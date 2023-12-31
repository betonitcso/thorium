resource "aws_dynamodb_table" "document_chunks_table" {
  name           = "document_chunks"
  billing_mode   = "PAY_PER_REQUEST"
  attribute {
    name = "document_id" # a unique hash of customer id + document id
    type = "S"
  }
  attribute {
    name = "chunk_id" # ID of chunk inside a document
    type = "N"
  }
  hash_key  = "document_id"
  range_key = "chunk_id"
}