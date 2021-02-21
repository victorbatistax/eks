resource "aws_vpc_peering_connection" "peering_lab" {
  peer_owner_id = var.account_id
  peer_region   = var.peer_region
  peer_vpc_id   = var.peer_vpc_id
  vpc_id        = aws_vpc.vpc_eks_lab.id

  tags = {
    Name           = "VPC Peering lab cluster and default vpc"
  }
}
