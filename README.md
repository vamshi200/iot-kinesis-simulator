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

### Why Simulate IoT Data?

In many cases, it's impractical or expensive to work with thousands of real IoT devices during development or testing. The **iot-kinesis-simulator** generates synthetic, realistic sensor data streams that mimic how real IoT devices produce data over time. This simulator helps developers prototype, test, and refine real-time data pipelines without relying on physical hardware.

### AWS Kinesis and Real-Time Streaming

AWS Kinesis is a managed service designed to handle real-time streaming data ingestion, processing, and analytics. The simulator pushes the generated IoT data into an AWS Kinesis data stream, enabling downstream services to process the data continuously. This mirrors real-world architectures where data is ingested from devices and immediately processed or stored.

---

## Project Components and Workflow

1. **Simulated IoT Data Generation**

   - The simulator produces synthetic sensor data such as temperature, humidity, location, and other relevant metrics.
   - Data is generated at realistic intervals, mimicking live IoT devices.
   - The simulator supports multiple virtual devices generating streams concurrently.

2. **Data Streaming to AWS Kinesis**

   - Simulated data is pushed into an AWS Kinesis data stream, which acts as a scalable, durable ingestion layer.
   - Kinesis ensures the continuous flow of data to downstream consumers.

3. **Real-Time Data Processing**

   - AWS Lambda functions or other consumer applications can process the streaming data in real time.
   - Examples include filtering, aggregating, transforming, or triggering alerts based on incoming data.

4. **Data Delivery and Storage**

   - Data from Kinesis can be delivered to storage services such as Amazon S3 using Kinesis Firehose.
   - This enables long-term storage, batch analysis, and integration with visualization tools.

5. **Visualization and Analytics (Optional)**

   - With stored data, users can build dashboards and analytics using AWS QuickSight or other BI tools.
   - This completes the full pipeline from device simulation to actionable insights.

---

## Why This Project Matters

IoT generates vast amounts of continuous data, making real-time processing essential for use cases like:

- **Anomaly Detection:** Identifying faults or unusual patterns immediately.
- **Predictive Maintenance:** Proactively servicing equipment before failures occur.
- **Live Monitoring:** Updating dashboards and alerts in real time for operational decisions.

Traditional batch processing methods cannot handle such high-velocity data effectively. Using AWS Kinesis and this simulator, developers can create robust streaming pipelines that process data with low latency, ensuring timely and reliable insights.

---

## Key Benefits and Use Cases

- **Cost-Effective Development:** No need for expensive IoT hardware to test streaming architectures.
- **Learning and Experimentation:** Hands-on experience with AWS streaming services and IoT data flows.
- **Prototyping Production Pipelines:** Test scalability and performance of streaming solutions before deployment.
- **Customizable Simulation:** Extend or modify sensor types and data patterns to fit specific domain requirements.

---

## Getting Started

(You can add your installation, setup, and usage instructions here — if you want, I can help you draft this too!)

---

## License

This project is licensed under the [MIT License](./LICENSE).

---

## Contributing

Feel free to submit issues, pull requests, or suggest new features to improve the simulator and make it more realistic and powerful.

---

## Contact

For questions or support, reach out to [Your Name or Email].

---

# Summary

The **iot-kinesis-simulator** offers a complete solution to simulate, stream, and process IoT sensor data using AWS Kinesis and related services. It empowers developers to build and test real-time data pipelines in a scalable, cost-effective, and realistic environment, advancing skills in cloud streaming architectures and IoT analytics.

---


