# nlu-french-benchmark

### French benchmark of NLU services for employee support use case during covid-19 pandemic. 

These datasets were created by the Wikit team in order to compare the performances of NLU tools on the French language. 

The dataset use case is employee support during the covid 19 pandemic. The intents and entities were defined to answer department employees' questions on the evolution of work conditions related to the crisis. 

- The _training_dataset.csv_ file contains training utterances with associated intent used to train NLU services. 

- The _test_dataset.csv_ file contains test utterances with associated intent used to test NLU services. 

### Upload on Hugging Face

Here are the commands to upload the dataset on Hugging Face.

```
python3 -m venv ./venv
source venv/bin/activate
pip install -r requirements.txt
huggingface-cli login
python3 upload_hugging_face.py
```
