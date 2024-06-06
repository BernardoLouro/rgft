<div align="center">
  
# [rule-gen-fine-tuning](https://github.com/BernardoLouro/rule-gen-fine-tuning)

</div>

<div align="center">
  
---

This projects acts as a tool to replicate the study found in the paper "Analysis of the Capability and Training of Chat Bots in the Generation of Rules for Firewall or Intrusion Detection Systems".
  
---

</div>

## Table of Contents
- [rule-gen-fine-tuning](#rule-gen-fine-tuning)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Requirements](#requirements)
  - [Datasets](#datasets)
  - [Scripts](#scripts)
  - [Notebook](#notebook)
  - [License](#license)
    - [Apache License 2.0](#apache-license-20)


## Introduction

This project can be used to replicate the study mentioned above. Below there is a brief description of every file available.


## Requirements

This project used Unsloth, follow their installation instructions here: [Unsloth](https://github.com/unslothai/unsloth).


## Datasets


dataset_a1.json -> Dataset used to fine-tune the model in approach one.


dataset_a2.json -> Dataset used to fine-tune the model in approach two.


dataset_a3.json -> Dataset used to fine-tune the model in approach three.


## Scripts


test-base-model.py -> Python script used to test Mistral-7B base model(it can be used to test any model available in [HuggingFace](https://huggingface.co/)).


test_model.py -> Python script used to test fine-tuned models.

rouge_metric.py -> Python script used to obtain the rouge score.


## Notebook


fine-tuning.ipynb -> Jupiter notebook used to fine-tune the Mistral-7B model, which followed the example given by [Unsloth](https://github.com/unslothai/unsloth).


## License

### Apache License 2.0

This project is licensed under the [Apache License 2.0](LICENSE). This license permits use, modification, distribution, and sublicense of the code for both private and commercial purposes, provided that the original copyright notice and a disclaimer of warranty are included in all copies or substantial portions of the software. It also requires a clear attribution back to the original author(s) of the repository. For more details, see the [LICENSE](LICENSE) file in this repository.
