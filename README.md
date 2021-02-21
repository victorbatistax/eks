# Laboratorio AWS EKS

**Author:** [Daniel Resende](https://github.com/dresende88)

O Laboratio surge na necessidade primaria de aprendizado e auxilio a comunidade.

## Pré requisistos

- Instalação das ferramentas
    - [Terraform](https://www.terraform.io/downloads.html)
    - [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
    - [Amazon EKS CLI](https://eksctl.io/introduction/#installation)
    - [Kubernetes CLI](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
    - [Python 3](https://www.python.org/downloads/)

- Configurações Necessarias
    - [Credenciais AWS](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)
    - Criar um arquivo chamado **terraform.tfvars** contendo os valores das variaveis necessarias para a execuçao do terraform.

            Exemplo: 
            
            aws_region = "us-east-1"
            vpc_cidr = "172.16.0.0/16"
            cluster_name = "lab-cluster"
            account_id = "0000000000"
            peer_vpc_id = "vpc-0000000"
            peer_region = "us-east-2"
            
    - Criar um arquivo [backend.tf](https://www.terraform.io/docs/language/settings/backends/s3.html) (opcional - caso não exista sera gerado um arquivo de controle na maquina de execução)

## Instalação das Bibliotecas Python
- execute o comando   -> `pip3 install jinja2`

## Construção do ambiente inicial

- Inicializão do terraform, nesse processo os modulos, providers são baixados e backend iniciado.

    `terraform init` 
- Verificação do Plano, fase onde é feito uma verificação previa antes da execução e provisionamento dos recursos. 

    `terraform plan` _( -refresh=true util, mas opcional )_
- Contrução do ambiente de forma efetiva, aqui iremos de fato aplicar o que foi planejado.

    `terraform apply` _( -auto-approve util, mas opcional )_

## Criação do Clustes EKS 

- Execute o script em python, mas antes verifique o que o mesmo se propoem a fazer.

    A execução se dá por meio do comando:

    `python3 gen_cluster_config_file.py`


## AGUARDE
:coffee: FAÇA UM CAFÉ E AGUARDE! :smoking:

## Antes de dormir, Exclua os recursos 

- Deletando o Node Group

     `eksctl delete nodegroup spot --cluster=lab-cluster --region us-east-1`
- Deletando o Cluster EKS

    `eksctl delete cluster lab-cluster --region us-east-1`
- Destruindo o ambiente provisionado com o terraform

    `terraform destroy`


## Links Uteis

- https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html

- https://eksctl.io/introduction/

- https://aws.github.io/aws-eks-best-practices/security/docs/

- https://docs.aws.amazon.com/eks/latest/userguide/fargate.html

- https://eksctl.io/usage/schema/
