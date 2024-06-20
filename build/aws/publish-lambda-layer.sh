pip install -r requirements.txt -t "./packages/python/lib/python3.10/site-packages"

(cd packages && zip -r ../package-layer.zip ./python)

echo Layer Version ARN: $(aws lambda publish-layer-version \
    --layer-name "${api_name}_base" \
    --zip-file "fileb://package-layer.zip" \
    --query "LayerVersionArn"
)

rm ./package-layer.zip
rm -r ./packages