auth_uri="arn:aws:apigateway:eu-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:eu-west-2:053630928262:function:${API_NAME}_auth:\${stageVariables.stageName}/invocations"
top_level_resources=("all-images-by-series" "login" "image" "image-data" "reorder")
declare -A top_level_ids

api_id=$(aws apigateway create-rest-api --name "$API_NAME" --query "id" --output "text")
root_resource_id=$(aws apigateway get-resources --rest-api-id "$api_id" --query "items[0].id"  --output "text")

# Authorizer
auth_id=$(aws apigateway create-authorizer \
    --rest-api-id "${api_id}" \
    --name "lambda_auth" \
    --type "TOKEN" \
    --authorizer-uri "${auth_uri}" \
    --identity-source "method.request.header.Authorization" \
    --query "id" \
    --output "text"
)

# Create resources
image_data_resource=$(aws apigateway create-resource \
    --rest-api-id "$api_id" \
    --parent-id "$root_resource_id" \
    --path-part "image-data" \
    --query "id" \
    --output "text"
)
image_data_id_resource=$(aws apigateway create-resource \
    --rest-api-id "$api_id" \
    --parent-id "${image_data_resource}" \
    --path-part "{id}" \
    --query "id" \
    --output "text"
)
image_resource=$(aws apigateway create-resource \
    --rest-api-id "$api_id" \
    --parent-id "$root_resource_id" \
    --path-part "image" \
    --query "id" \
    --output "text"
)
image_id_resource=$(aws apigateway create-resource \
    --rest-api-id "$api_id" \
    --parent-id "${image_resource}" \
    --path-part "{id}" \
    --query "id" \
    --output "text"
)
login_resource=$(aws apigateway create-resource \
    --rest-api-id "$api_id" \
    --parent-id "$root_resource_id" \
    --path-part "login" \
    --query "id" \
    --output "text"
)

# Create lambda methods
http_method="GET"
path="image-data"
resource_id=$image_data_resource
lambda_name="${API_NAME}_${path}_${http_method}"
aws apigateway put-method \
    --rest-api-id "$api_id" \
    --resource-id "$resource_id" \
    --http-method "$http_method" \
    --authorization-type "NONE"

aws apigateway put-integration \
    --rest-api-id "$api_id" \
    --resource-id "$resource_id" \
    --http-method "$http_method" \
    --type "AWS_PROXY" \
    --integration-http-method "POST" \
    --uri "arn:aws:apigateway:eu-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:eu-west-2:053630928262:function:$lambda_name:\${stageVariables.stageName}/invocations"
stages=("live" "dev")
for stage in "${stages[@]}"; do
    aws lambda add-permission \
        --function-name "arn:aws:lambda:eu-west-2:053630928262:function:$lambda_name:${stage}" \
        --source-arn "arn:aws:execute-api:eu-west-2:053630928262:$api_id/*/$http_method/$path" \
        --principal apigateway.amazonaws.com \
        --statement-id Allow-API_Invoke-Access \
        --action lambda:InvokeFunction
done

http_method="PUT"
path="image-data"
resource_id=$image_data_resource
lambda_name="${API_NAME}_${path}_${http_method}"
aws apigateway put-method \
    --rest-api-id "$api_id" \
    --resource-id "$resource_id" \
    --http-method "$http_method" \
    --authorization-type "CUSTOM" \
    --authorizer-id "$auth_id"

aws apigateway put-integration \
    --rest-api-id "$api_id" \
    --resource-id "$resource_id" \
    --http-method "$http_method" \
    --type "AWS_PROXY" \
    --integration-http-method "POST" \
    --uri "arn:aws:apigateway:eu-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:eu-west-2:053630928262:function:$lambda_name:\${stageVariables.stageName}/invocations"
stages=("live" "dev")
for stage in "${stages[@]}"; do
    aws lambda add-permission \
        --function-name "arn:aws:lambda:eu-west-2:053630928262:function:$lambda_name:${stage}" \
        --source-arn "arn:aws:execute-api:eu-west-2:053630928262:$api_id/*/$http_method/$path" \
        --principal apigateway.amazonaws.com \
        --statement-id Allow-API_Invoke-Access \
        --action lambda:InvokeFunction
done

http_method="POST"
path="image-data"
resource_id=$image_data_resource
lambda_name="${API_NAME}_${path}_${http_method}"
aws apigateway put-method \
    --rest-api-id "$api_id" \
    --resource-id "$resource_id" \
    --http-method "$http_method" \
    --authorization-type "CUSTOM" \
    --authorizer-id "$auth_id"

aws apigateway put-integration \
    --rest-api-id "$api_id" \
    --resource-id "$resource_id" \
    --http-method "$http_method" \
    --type "AWS_PROXY" \
    --integration-http-method "POST" \
    --uri "arn:aws:apigateway:eu-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:eu-west-2:053630928262:function:$lambda_name:\${stageVariables.stageName}/invocations"
stages=("live" "dev")
for stage in "${stages[@]}"; do
    aws lambda add-permission \
        --function-name "arn:aws:lambda:eu-west-2:053630928262:function:$lambda_name:${stage}" \
        --source-arn "arn:aws:execute-api:eu-west-2:053630928262:$api_id/*/$http_method/$path" \
        --principal apigateway.amazonaws.com \
        --statement-id Allow-API_Invoke-Access \
        --action lambda:InvokeFunction
done

http_method="PUT"
path="{id}"
resource_id=$image_data_id_resource
lambda_name="${API_NAME}_image-data_id_${http_method}"
aws apigateway put-method \
    --rest-api-id "$api_id" \
    --resource-id "$resource_id" \
    --http-method "$http_method" \
    --authorization-type "CUSTOM" \
    --authorizer-id "$auth_id"

aws apigateway put-integration \
    --rest-api-id "$api_id" \
    --resource-id "$resource_id" \
    --http-method "$http_method" \
    --type "AWS_PROXY" \
    --integration-http-method "POST" \
    --uri "arn:aws:apigateway:eu-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:eu-west-2:053630928262:function:$lambda_name:\${stageVariables.stageName}/invocations"
stages=("live" "dev")
for stage in "${stages[@]}"; do
    aws lambda add-permission \
        --function-name "arn:aws:lambda:eu-west-2:053630928262:function:$lambda_name:${stage}" \
        --source-arn "arn:aws:execute-api:eu-west-2:053630928262:$api_id/*/$http_method/$path" \
        --principal apigateway.amazonaws.com \
        --statement-id Allow-API_Invoke-Access \
        --action lambda:InvokeFunction
done

http_method="DELETE"
path="{id}"
resource_id=$image_id_resource
lambda_name="${API_NAME}_image_id_${http_method}"
aws apigateway put-method \
    --rest-api-id "$api_id" \
    --resource-id "$resource_id" \
    --http-method "$http_method" \
    --authorization-type "CUSTOM" \
    --authorizer-id "$auth_id"

aws apigateway put-integration \
    --rest-api-id "$api_id" \
    --resource-id "$resource_id" \
    --http-method "$http_method" \
    --type "AWS_PROXY" \
    --integration-http-method "POST" \
    --uri "arn:aws:apigateway:eu-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:eu-west-2:053630928262:function:$lambda_name:\${stageVariables.stageName}/invocations"
stages=("live" "dev")
for stage in "${stages[@]}"; do
    aws lambda add-permission \
        --function-name "arn:aws:lambda:eu-west-2:053630928262:function:$lambda_name:${stage}" \
        --source-arn "arn:aws:execute-api:eu-west-2:053630928262:$api_id/*/$http_method/$path" \
        --principal apigateway.amazonaws.com \
        --statement-id Allow-API_Invoke-Access \
        --action lambda:InvokeFunction
done

http_method="POST"
path="login"
resource_id=$login_resource
lambda_name="${API_NAME}_${path}_${http_method}"
aws apigateway put-method \
    --rest-api-id "$api_id" \
    --resource-id "$resource_id" \
    --http-method "$http_method" \
    --authorization-type "NONE"

aws apigateway put-integration \
    --rest-api-id "$api_id" \
    --resource-id "$resource_id" \
    --http-method "$http_method" \
    --type "AWS_PROXY" \
    --integration-http-method "POST" \
    --uri "arn:aws:apigateway:eu-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:eu-west-2:053630928262:function:$lambda_name:\${stageVariables.stageName}/invocations"
stages=("live" "dev")
for stage in "${stages[@]}"; do
    aws lambda add-permission \
        --function-name "arn:aws:lambda:eu-west-2:053630928262:function:$lambda_name:${stage}" \
        --source-arn "arn:aws:execute-api:eu-west-2:053630928262:$api_id/*/$http_method/$path" \
        --principal apigateway.amazonaws.com \
        --statement-id Allow-API_Invoke-Access \
        --action lambda:InvokeFunction
done


# S3 integration
http_method="PUT"
path="{id}"
resource_id=$image_id_resource
lambda_name="${API_NAME}_image_id_${http_method}"
s3roleARN=$(aws iam create-role \
    --role-name "${API_NAME}s3PutRole" \
    --path "/${API_NAME}/" \
    --assume-role-policy-document "{\"Version\": \"2012-10-17\",\"Statement\": [{\"Sid\": \"\",\"Effect\": \"Allow\",\"Principal\": {\"Service\": [\"apigateway.amazonaws.com\"]},\"Action\": [\"sts:AssumeRole\"]}]}" \
    --query "Role.Arn" \
    --output "text"
)
s3policyARN=$(aws iam create-policy \
    --policy-name "${API_NAME}-apigateway-put-s3" \
    --policy-document "{\"Version\": \"2012-10-17\",\"Statement\": [{\"Sid\": \"APIGWPutAllow\",\"Effect\": \"Allow\",\"Action\": \"s3:PutObject\",\"Resource\": \"arn:aws:s3:::${API_NAME}/*\"}]}" \
    --query "Policy.Arn" \
    --output "text"
)
aws iam attach-role-policy \
    --role-name "${API_NAME}s3PutRole" \
    --policy-arn "${s3policyARN}"
aws apigateway put-method \
    --rest-api-id "$api_id" \
    --resource-id "$resource_id" \
    --http-method "$http_method" \
    --authorization-type "CUSTOM" \
    --authorizer-id "$auth_id" \
    --request-parameters "method.request.path.id=true" 
aws apigateway put-integration \
    --rest-api-id "$api_id" \
    --resource-id "$resource_id" \
    --http-method "$http_method" \
    --credentials "${s3roleARN}"\
    --type "AWS" \
    --integration-http-method "PUT" \
    --uri "arn:aws:apigateway:eu-west-2:${API_NAME}.s3:path/${API_NAME}/{artist}/{id}"\
    --request-parameters "integration.request.path.id=method.request.path.id"

aws apigateway create-deployment \
    --rest-api-id "$api_id" \
    --stage-name "live" \
    --variables "stageName=live" 
    
aws apigateway create-deployment \
    --rest-api-id "$api_id" \
    --stage-name "dev" \
    --variables "stageName=dev"