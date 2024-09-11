# Online Grooming Project

The project is to design and prototype a chatbot Neeko to fulfill the goal of online grooming prevention.

## Overview of the files

`code/` - code to set up the chatbot 

`document/` - documents for this project

`line-chatbot-data/` - data for setting LINE official account of the chatbot

`survey-data/` - data for parent and child survey

## Usage

### eSPD Model Evaluation

Change the current working directory.

```bash
cd code/model-eval/
```

Setting up library dependencies for the code.

```bash
pip install -r requirements.txt
```

Then, run the code to get f1-score, precision, recall and accuracy of the model in `code/model-eval/resources/`

```bash
python ./evaluate_f1.py
```

The result will store at `score.txt` in `resources` folder.

You can learn more about the codes by [eSPD LAB project](https://gitlab.com/early-sexual-predator-detection/eSPD-lab).

### Setup the Chatbot

1. Create and setup a dilogflow CX agent by importing `code/dialogflow-cx-agent/`.
2. Deploy the eSPD model `code/model-api/` as REST API on server. (You can deploy on [GCP](https://cloud.google.com/docs) or other platforms)
3. Deploy  all webhooks in `code/dialogflow-cx-webhook/` on Google Cloud Functions.
4. Setup the webhook URL for dilogflow CX agent.
5. Integrate the Dialogflow CX agent with LINE. (See the [
documentation](https://cloud.google.com/dialogflow/cx/docs/concept/integration/line)) 
 

## Reference

- [Early Detection of Sexual Predators in Chats](https://early-sexual-predator-detection.gitlab.io/)
- Dialogflow CX [documentation](https://cloud.google.com/dialogflow/cx/docs)
- Google Cloud Functions [documentation](https://cloud.google.com/functions/docs)
- [LINE Developers](https://developers.line.biz/en/)



