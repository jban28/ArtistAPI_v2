funcs_to_deploy=($FUNCS_TO_DEPLOY)

for func_file in "${funcs_to_deploy[@]}"
do
    func_name="${func_file/.py/}"
    func_name="artist-api-lambda_${func_name##*/}"

    zip -j lambda.zip $func_file
    aws lambda update-function-code --function-name="${func_name}" --zip-file=fileb://lambda.zip
    aws lambda publish-version --function-name="${func_name}"
done