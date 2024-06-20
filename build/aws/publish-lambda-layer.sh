pip install -r requirements.txt -t "/package-layer/python/lib/python3.10/site-packages"

zip -r package-layer.zip ./package-layer

echo $(aws lambda publish-layer-version \
    --layer-name "${api_name}_base" \
    --zip-file "fileb://package-layer.zip" \
    --query "layer-version-arn"
)