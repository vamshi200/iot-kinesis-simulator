![CI](https://github.com/vamshi200/iot-kinesis-simulator/actions/workflows/deploy.yml/badge.svg)

# IoT Kinesis Data Pipeline 🚀

This project simulates IoT sensor data and builds a real-time streaming data pipeline using **AWS Kinesis**, **AWS Lambda**, **Amazon S3**, and **Athena**. It is fully automated with **GitHub Actions CI/CD**.

---

## 📌 Features

- Simulates IoT sensor data (temperature, humidity).
- Sends data to Kinesis Data Stream & Firehose.
- Processes data using AWS Lambda.
- Stores structured data in Amazon S3.
- Query data using Amazon Athena.
- CI/CD automation with GitHub Actions.

---

## 🛠️ Technologies Used

- Python 3.9
- AWS Kinesis Data Stream & Firehose
- AWS Lambda
- Amazon S3
- AWS IAM
- Amazon Athena
- GitHub Actions

---

## 📁 Project Structure

```bash
.
├── send_data.py            # Python script to simulate and send data
├── manifest.json           # Athena manifest for JSON S3 data
└── .github/
    └── workflows/
        └── deploy.yml      # CI/CD pipeline using GitHub Actions

