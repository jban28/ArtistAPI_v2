lambda_funcs=($(ls src/lambda-functions/*.py))
layer_arn=$1

for func_file in "${lambda_funcs[@]}"; do
    func_name="${func_file/.py/}"
    func_name="${API_NAME}_${func_name##*/}"

    aws iam create-role \
        --role-name "${func_name}_lambda-role" \
        --path "/${API_NAME}/" \
        --assume-role-policy-document "file://build/aws/lambda-execution-role.json" \
        --query "Role.Arn" \
        --output "text"

done

# Separate loop with time delay to allow IAM roles to propagate
sleep 10s

for func_file in "${lambda_funcs[@]}"; do
    func_name="${func_file/.py/}"
    func_name="${API_NAME}_${func_name##*/}"

    rm lambda_function.zip
    zip -j lambda_function.zip $func_file

    aws lambda create-function \
    --function-name "$func_name" \
    --runtime "python3.10" \
    --role  "arn:aws:iam::053630928262:role/${API_NAME}/${func_name}_lambda-role" \
    --zip-file "fileb://lambda_function.zip" \
    --handler "${func_name}.lambda_handler" \
    --layers "$layer_arn" \
    --environment "Variables={databaseURI=$DATABASE_URI,rootURL=https://artist-api.s3.amazonaws.com}" 

    aws lambda create-alias \
    --function-name "$func_name" \
    --name "live" \
    --function-version "\$LATEST"

    aws lambda create-alias \
    --function-name "$func_name" \
    --name "dev" \
    --function-version "\$LATEST" 

done

rm lambda_function.zip

# Function specific configuration
aws lambda update-function-configuration \
    --function-name "${API_NAME}_authenticate" \
    --environment "Variables={databaseURI=$DATABASE_URI,rootURL=https://artist-api.s3.amazonaws.com,secretKey=$SECRET_KEY}"

aws lambda update-function-configuration \
    --function-name "${API_NAME}_login_POST" \
    --environment "Variables={databaseURI=$DATABASE_URI,rootURL=https://artist-api.s3.amazonaws.com,secretKey=$SECRET_KEY}"