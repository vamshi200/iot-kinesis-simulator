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


## 📄 License

This project is licensed under the [MIT License](./LICENSE).
# IoT Kinesis Simulator

## Project Overview

The **iot-kinesis-simulator** project is designed to simulate real-world Internet of Things (IoT) sensor data streams and process them in real time using **AWS Kinesis** and related AWS services. It replicates the behavior of thousands of IoT devices generating continuous streams of sensor data, enabling developers to build, test, and demonstrate scalable, real-time data streaming pipelines without needing physical IoT hardware.

---

## Main Theme and Purpose

### What is IoT?

IoT (Internet of Things) refers to a network of physical devices embedded with sensors, software, and connectivity that collect and exchange data. Common examples include temperature sensors, smart meters, motion detectors, and industrial equipment. These devices generate data continuously, producing a large volume of time-series data that requires efficient, real-time processing.
# IoT Kinesis Simulator

## 📘 Project Overview

The **IoT Kinesis Simulator** is a real-time data streaming pipeline built using AWS services that simulates IoT devices generating live sensor data. This project is ideal for developers and data engineers who want to learn or demonstrate how to build scalable, cloud-native streaming data pipelines using services like **AWS Kinesis**, **Lambda**, **Firehose**, and **S3**.

---

## 🎯 Real-World Use Case: Smart Manufacturing Monitoring System

In a real-world manufacturing plant, thousands of machines are fitted with IoT sensors. These sensors track data like:

* Temperature
* Vibration
* Pressure
* Energy consumption
* Runtime status

To **prevent downtime**, **predict failures**, and **optimize operations**, this telemetry data must be:

* ✅ Collected in real-time
* ✅ Processed for anomalies
* ✅ Stored for historical analysis
* ✅ Visualized for monitoring

However, deploying and testing such systems in production can be expensive and complex. **This project simulates this entire use case**, giving you a fully working real-time data pipeline without needing physical devices.

---

## 🧱 System Architecture

```text
+-------------------+        +---------------------+        +------------------------+        +-------------------+
|  IoT Simulator     | ----> |  AWS Kinesis Stream  | ----> | AWS Lambda (Optional)  | ----> | AWS Kinesis Firehose |
+-------------------+        +---------------------+        +------------------------+        +-------------------+
                                                                                                     |
                                                                                                     v
                                                                                               +-----------------+
                                                                                               |    Amazon S3     |
                                                                                               +-----------------+
```

---

## ⚙️ Components

### 1. IoT Simulator (Node.js)

* Simulates multiple IoT devices (e.g., 1000+ virtual sensors)
* Sends randomly generated data like:

```json
{
  "deviceId": "sensor-102",
  "timestamp": "2025-06-21T12:34:56Z",
  "temperature": 28.7,
  "humidity": 65.3,
  "status": "active"
}
```

* Sends data at regular intervals to AWS Kinesis using AWS SDK

### 2. AWS Kinesis Data Stream

* Captures incoming records from the simulator
* Designed to scale to millions of events per second

### 3. AWS Lambda (Optional)

* Processes each record: filtering, transformation, or enrichment
* Can trigger alerts, route based on data type, or enrich with metadata

### 4. AWS Kinesis Firehose

* Buffers and batches data from the stream
* Delivers raw or processed data to Amazon S3

### 5. Amazon S3

* Stores JSON files partitioned by time for long-term retention
* Can be queried using Athena or visualized in QuickSight

---

## 🚀 Key Features

* ✅ Simulates real-world IoT sensor behavior
* ✅ Fully event-driven and serverless
* ✅ Easy to deploy, customize, and scale
* ✅ No hardware required – all virtual and cloud-native
* ✅ Real-time + batch-compatible (Kinesis + S3)

---

## 🛠️ Technologies Used

| Tool         | Purpose                             |
| ------------ | ----------------------------------- |
| Node.js      | IoT data simulation (sender script) |
| AWS Kinesis  | Real-time stream ingestion          |
| AWS Lambda   | Optional real-time processing       |
| AWS Firehose | Delivery stream to storage          |
| Amazon S3    | Persistent storage for data         |
| AWS CLI/IAM  | Security and access control         |
| Terraform    | Infrastructure as Code (IaC)        |
| QuickSight   | Real-time visualization dashboards  |

---

## 🔎 How to Use

### 1. Clone the Repo

```bash
git clone https://github.com/vamshik/iot-kinesis-simulator.git
cd iot-kinesis-simulator
```

### 2. Configure AWS Credentials

Make sure your terminal is authenticated with AWS CLI and has permissions for:

* Kinesis
* Firehose
* Lambda (if used)
* S3

```bash
aws configure
```

### 3. Deploy AWS Infrastructure (Terraform Example)

Use the provided `infra/terraform` folder to create:

* Kinesis Data Stream
* Firehose Delivery Stream
* S3 Bucket

```bash
cd infra/terraform
terraform init
terraform apply
```

### 4. Run the Simulator

```bash
node simulate.js
```

This script will continuously push synthetic IoT data to your Kinesis stream.

---

## 📊 Example Output in S3

Your data will appear in your S3 bucket in paths like:

```
s3://your-bucket-name/year=2025/month=06/day=21/...
```

Each file contains multiple JSON records like:

```json
{"deviceId":"sensor-45","temperature":26.5,"humidity":60.3,"timestamp":"2025-06-21T14:11:22Z"}
```

---

## 💡 Why This Project Is Important

* Learn real-world **data engineering** skills
* Prototype **real-time IoT systems** affordably
* Build a foundation for **smart city**, **healthcare**, **transport**, or **industrial monitoring** use cases
* Demonstrates mastery in **cloud architecture**, **event-driven design**, and **serverless computing**

---

## 📄 License

This project is licensed under the [MIT License](./LICENSE)

---

## 🙌 Contributions

Pull requests are welcome! If you have ideas to extend the simulator (more sensors, API integration, dashboard UI), feel free to fork and improve.

---

## 📨 Contact

**Author:** Vamshi
**GitHub:** [vamshik](https://github.com/vamshik)

---

## ⭐ Summary

**iot-kinesis-simulator** offers a hands-on, real-time simulation of how modern cloud-based data systems work — enabling anyone to understand, test, and showcase IoT streaming pipelines using real AWS services. It’s simple, powerful, and production-relevant.

