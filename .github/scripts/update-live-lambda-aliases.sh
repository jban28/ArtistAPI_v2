func_files=($(ls src/lambda-functions/*.py))
for file in "${func_files[@]}"
do
    func_name="${func_file/.py/}"
    func_name="artist-api-lambda_${func_name##*/}"

    func_version=$(aws lambda get-alias \
        --function-name="${func_name}" \
        --name "dev" \
        --query "FunctionVersion" \
        --output "text"
    )

    aws lambda update-alias \
        --function-name="${func_name}" \
        --name "live" \
        --function-version "${func_version}"
done