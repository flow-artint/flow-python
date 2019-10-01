# Flow Python Client API

Get started by obtaining your API key from official [webpage](https://theflowai.com).

### Installation

Clone this repository

```bash
git clone https://github.com/flow-artint/flow_ai.git
```

Install this package from `flow_ai` directory

```bash
cd flow_ai
pip install .
```
Use `sudo` with `pip` above, if required.

### Usage

Simple demo of how to use this package for face detection. 

```python
from flow_ai import FlowApp, Model

app = FlowApp(api_key="YOUR_API_KEY")

# Setup some variables
input_url = "https://qph.fs.quoracdn.net/main-qimg-53a3aa40f0b577ac69588681fb60d0c3-c"
model_name = Model.FACE_DETECTION

# Now, make the prediction
prediction = app.predict_by_url(input_url, model_name)

# Get results
(status_code, result) = prediction["status_code"], prediction["result"]
bounding_box = result[0][:4]
confidence_score = result[0][-1]

print(f'status_code: {status_code}')
print(f'result: {result[0]}')
print(f"bounding_box: {bounding_box}")
print(f"confidence_score: {confidence_score}")
```

Prints the following:
```
status_code: 200
result: [315.84075927734375, 56.2187385559082, 370.674560546875, 128.3153839111328, 0.9999943971633911]
bounding_box: [315.84075927734375, 56.2187385559082, 370.674560546875, 128.3153839111328]
confidence_score: 0.9999943971633911
```

See [documentation](https://docs.theflow_ai.com) for detailed explanation.