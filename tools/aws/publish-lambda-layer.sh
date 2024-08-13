pip install -r requirements.txt -t "./packages/python/lib/python3.10/site-packages"

(cd packages && zip -r ../package-layer.zip ./python)

echo Layer Version ARN: $(aws lambda publish-layer-version \
    --layer-name "${API_NAME}_base" \
    --zip-file "fileb://package-layer.zip" \
    --compatible-runtimes "python3.10" \
    --query "LayerVersionArn"
)

rm ./package-layer.zip
rm -r ./packages