//Outputs VPC Values

output "vpc_id" {
    description = "The ID od the VPC"
    value = concat(aws_vpc.vpc_eks_lab.*.id, [""])[0]
  
}

output "vpc_arn" {
  description = "The ARN of the VPC"
  value       = concat(aws_vpc.vpc_eks_lab.*.arn, [""])[0]
}

output "vpc_cidr_block" {
  description = "The CIDR block of the VPC"
  value       = concat(aws_vpc.vpc_eks_lab.*.cidr_block, [""])[0]
}


// Subnets Publicas
output "public_subnets" {
  description = "List of IDs of public subnets"
  value       = aws_subnet.public_lab.*.id
}

output "public_subnet_arns" {
  description = "List of ARNs of public subnets"
  value       = aws_subnet.public_lab.*.arn
}

// Subnets Privadas
output "private_subnets" {
  description = "List of IDs of private subnets"
  value       = aws_subnet.private_lab.*.id
}

output "private_subnet_arns" {
  description = "List of ARNs of private subnets"
  value       = aws_subnet.private_lab.*.arn
}

// security_group_id

output "ingress_sg_security_group_id" {
  description = "The ID of the security group"
  value = concat(aws_security_group.ingress_sg.*.id, [""]) [0]
}

output "node_sg_security_group_id" {
  description = "The ID of the security group"
  value = concat(aws_security_group.node_sg.*.id, [""]) [0]
}
output "eks_cluster_security_group_id" {
  description = "The ID of the security group"
  value = concat(aws_security_group.eks_cluster.*.id, [""]) [0]
}
output "ingress_private_sg_security_group_id" {
  description = "The ID of the security group"
  value = concat(aws_security_group.ingress_private_sg.*.id, [""]) [0]
}

// IAM

output "eks_cluster_aws_iam_role_arn" {
    description = "The ID of the eks cluster iam role"
    value = concat(aws_iam_role.eks_cluster.*.arn, [""])[0]
}

output "eks_node_aws_iam_role_arn" {
    description = "The ID of the eks cluster iam role"
    value = concat(aws_iam_role.eks_node.*.arn, [""])[0]
}

output "eks_node_aws_iam_instance_profile_arn" {
    value = concat(aws_iam_instance_profile.ProfileIAMRole.*.arn, [""])[0]
}

output "aws_public_keypair_name" {
    value = var.aws_public_keypair_name 
}