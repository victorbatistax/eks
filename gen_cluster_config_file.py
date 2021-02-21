import json, jinja2, os

os.system('terraform output -json > output_json_file.json')

with open("output_json_file.json") as json_file:
    outputs = json.load(json_file)


data = {
  "eks_cluster_security_group_id" : outputs['eks_cluster_security_group_id']['value'],
  "eks_cluster_security_group_id" : outputs['node_sg_security_group_id']['value'],
  "private_subnets_a" : '{ id: ' + outputs['private_subnets']['value'][0] +  ' }',
  "private_subnets_b" : '{ id: ' + outputs['private_subnets']['value'][1] +  ' }',
  "public_subnets_a" : '{ id: ' + outputs['public_subnets']['value'][0] +  ' }',
  "public_subnets_b" : '{ id: ' + outputs['public_subnets']['value'][1] +  ' }',
  "vpc_id" : outputs['vpc_id']['value'],
  "vpc_cidr_block" : outputs['vpc_cidr_block']['value'],
  "eks_cluster_aws_iam_role_arn" : outputs['eks_cluster_aws_iam_role_arn']['value'],
  "eks_node_aws_iam_instance_profile_arn" : outputs['eks_node_aws_iam_instance_profile_arn']['value'],
  "eks_node_aws_iam_role_arn" : outputs['eks_node_aws_iam_role_arn']['value'],
  "aws_public_keypair_name" : outputs['aws_public_keypair_name']['value'],
}


templateLoader = jinja2.FileSystemLoader(searchpath="./_eks_configs/")
templateEnv = jinja2.Environment(loader=templateLoader)
CLUSTER_TEMPLATE_FILE = "cluster.yaml"
NODEGROUP_SPOT_TEMPLATE_FILE = "nodes-spot.yaml"
template_cluster = templateEnv.get_template(CLUSTER_TEMPLATE_FILE)
template_nodegroup = templateEnv.get_template(NODEGROUP_SPOT_TEMPLATE_FILE)

cluster_conf_file = template_cluster.render(data)
nodegroups_conf_file = template_nodegroup.render(data)

# to save the results
with open("./_eks_configs/cluster-final.yaml", "w") as fh:
    fh.write(cluster_conf_file)


# to save the results
with open("./_eks_configs/node-spot-final.yaml", "w") as fh:
    fh.write(nodegroups_conf_file)


os.system('eksctl create cluster --config-file=./_eks_configs/cluster-final.yaml')

os.system('aws eks --region us-east-1 update-kubeconfig --name lab-cluster')

os.system('eksctl create nodegroup --config-file=./_eks_configs/node-spot-final.yaml')

os.system('eksctl utils update-kube-proxy --cluster lab-cluster --region us-east-1 --approve')
os.system('eksctl utils update-aws-node --cluster lab-cluster --region us-east-1 --approve')
os.system('eksctl utils update-coredns --cluster lab-cluster --region us-east-1 --approve')

os.system('kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.4.2/components.yaml')

os.system('kubectl apply -f ./manifests/alb-ingress-controller/rbac-role.yaml')
os.system('kubectl apply -f ./manifests/alb-ingress-controller/alb-ingress-controller.yaml')
os.system('kubectl apply -f ./manifests/cluster-autoscaler/cluster-autoscaler-autodiscover.yaml')

os.system('kubectl get pods -A')