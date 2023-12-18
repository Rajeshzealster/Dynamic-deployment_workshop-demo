# FogDEFTKube: An Extended FogDEFT Framework Supporting Kubernetes and Continuous Integration

## Project Overview

FogDEFTKube is an extended framework built upon the OASIS - Topology and Orchestration Specification for Cloud Applications (TOSCA) tailored for fog computing. This framework provides a user-friendly paradigm to model and dynamically deploy fog services remotely and on-demand. FogDEFTKube maintains four essential layers of abstraction:

1. **Platform Independence:** Utilizes Docker Containerization technology for seamless deployment across different platforms.

3. **Interoperability:** Leverages Kubernetes features to establish seamless inter-service communication and orchestration.

4. **Portability:** Incorporates TOSCA, a vendor-neutral modeling language, ensuring flexibility and compatibility with various cloud providers.
   ![Orchestration](https://github.com/Rajeshzealster/FogDEFTKube--Intelli-Climate-Case-study/assets/97143348/114be889-8810-45c9-a0ae-2e9eb6532256)


# Dynamic Deployment Workshop Demo
   ![workshop_hw-design](https://github.com/Rajeshzealster/Dynamic-deployment_workshop-demo/assets/97143348/8cacacd2-eab6-4317-8f72-62d8394f7576)

This repository contains the code for the IntelliClimate case study, showcasing dynamic deployment on fog infrastructure using xOpera orchestrator.

## Setup xOpera
1. Install xOpera from pip directly.
      ```bash
      pip install opera
      ```
   # (OR)

1. Update package information and install required packages:

   ```bash
   sudo apt update
   sudo apt install -y python3-venv python3-wheel python-wheel-common
   ```
2. Create a directory for xOpera and set up a virtual environment:
   ```bash
   mkdir ~/opera && cd ~/opera
   python3 -m venv .venv && . .venv/bin/activate
   pip install --upgrade pip
   pip install opera
   ```
## Setup Passwordless SSH
1. Generate SSH key:
   ```bash
   ssh-keygen
   ```
2. Copy SSH key to remote fog infrastructure (all nodes specified in inputs.yaml file):
   ```bash
   ssh-copy-id root@fog-node-1_IP
   ssh-copy-id root@fog-node-2_IP
   ```
## Clone the Repository
   ```bash
   git clone https://github.com/Rajeshzealster/Dynamic-deployment_workshop-demo.git
   cd Dynamic-deployment_workshop-demo
   ```
## Deploy Services
Use the xOpera CLI commands to deploy services onto fog infrastructure:
1. Validate the deployment:
   ```bash
      opera validate -i inputs.yaml service.yaml
   ```
2. Deploy the services
   ```bash
   opera deploy -i inputs.yaml service.yaml
   ```
2. Undeploy the services
   ```bash
   opera undeploy
   ```
## Observations
After deploying the IntelliClimate case study, observe the following:

# On node1 (Master Node)
Check the k3s cluster status:
   ```bash
   kubectl get nodes
   ```
View kubernetes objects.
   ```bash
   kubectl get deployments
   kubectl get pods
   kubectl get services
   ```
# On node4
Check the status of mqtt-publisher-service:
   ```bash
   systemctl status mqtt-publisher-service
   ```
# On node3
Check the status of the actuator service:
   ```bash
   systemctl status actuator
   ```
## Sensor Data Visualization
Install mosquitto-clients on any fog node:
   ```bash
   apt-get install mosquitto-clients
   ```
Subscribe to sensor/data topic:
   ```bash
   mosquitto_sub -h node1_IP -p 30001 -t sensor/data
   ```
Now, you can observe the sensor-generated values on the mqtt-server’s sensor/data topic.

We had setup the thresholds of 30 and 70 for temperature and humidity respectively. So, whenever the values goes beyond the threshold, you can see the actuator (here the servomotor) performing some work (rotates on to left for opening).









