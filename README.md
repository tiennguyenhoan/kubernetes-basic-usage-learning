# Kubernetes usage basic learning

## Inspiration:

I saw many people who want to learn with Kubernetes but they don't have much time for reading a bunch of definitions to understand how it works.
Or just because many tutorials focus too much on explaining all the definitions of Kubernetes and examples aren't focused on what they exactly want, deploy a simple application from End to End

Therefore, I made this small project with the aiming to support those, who want to learn k8s but don't have much time, to have the basic mindset of how Kubernetes works and how to work with it.
In this guideline, we will cover basic knowledge of K8s with step by step examples and I hope this can help other beginners

- We won't go depth into Docker in this guideline, but some basic knowledge in Docker and dockerize will be required. You can go to [Docker get started](https://docs.docker.com/get-started/) for a quick review about docker before we can move on
- I will try to avoid as much definition as I can in this tutorials, and I will focus more on practical examples with commands and explainations at that state, so if you need to know the definition and stuff, please the link **Kubernetes documentation** above

If you want to learn fully about Kubernetes please read [Kubernetes documentation](https://kubernetes.io/docs/tutorials/)

> **Importants**:
>
>   When you go through this guideline, you may see many explanations that may not correct 100% with the definitions on the official Documentation, since the target of this project is helping people have the general/basic knowledge on K8s.
>   Therefore, I made this as simple as I can, and some of them are the simple conclusion about my experience in Kubernetes.
>
>   Please let me know if any part of this guideline have incorrect, all of contributions are really appreciated to make this guideline better


<!-- vim-markdown-toc GFM -->

* [Requirement](#requirement)
* [Docker - Basic knowleged before we start](#docker---basic-knowleged-before-we-start)
  * [What is Docker](#what-is-docker)
  * [Learning Resource](#learning-resource)
* [Kubernetes](#kubernetes)
  * [What is Kubernetes](#what-is-kubernetes)
  * [Hardware level concept](#hardware-level-concept)
  * [Software level concept](#software-level-concept)
* [Software level practical](#software-level-practical)
    * [Ex-1: Simple deployment sample](#ex-1-simple-deployment-sample)
    * [Ex-2: containers comunication between deployment](#ex-2-containers-comunication-between-deployment)
    * [Ex-3: Deployment with multiple Containers in a pod](#ex-3-deployment-with-multiple-containers-in-a-pod)
    * [Ex-4:](#ex-4)

<!-- vim-markdown-toc -->

## Requirement

To follow this guideline, you must have:
- Docker installed in your machine, check [Docker install](https://docs.docker.com/engine/install/) if you don't have it

- Docker Desktop with Kubernetes activated or Minikube
  - Docker Desktop: Read [Docker Deskop - Kubernetes](https://docs.docker.com/desktop/kubernetes/) for how to enable K8s
  - Minikube: If you don't have kubernetes in your Docker Desktop, then follow [Minikube](https://github.com/kubernetes/minikube) to install it.

- kubectl command which will use most of the time to work with Kubernetes, check [Kubernetes install tools](https://kubernetes.io/docs/tasks/tools/)

## Docker - Basic knowleged before we start

If you want to learn of use Kubernetes, you must know how to work with Docker first. It's because Kubernetes will host your service/application as an Docker containers from Docker image.
By that, we will need to understand how to Dockerize an application and understand to work/troubleshoot a Docker container first 

### What is Docker

Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly.
With the feature or Docker, you can package your application with it's requires environments, this can be a few libraries or any filesystem of an installed operating system.
Then we can deploy it to any servers without concerns in installing librarys or configurating server's system

There are three main Docker components we will forcus on this tutorials:

Images :— A Docker based container image is something you package your application and its environment. It contains the filesystem that will be available to the application and other metadata, such as the path to the executable that should be executed when the image is run.

Registries :- A Docker Registry is a repository that stores your Docker images and facilitates easy sharing of those images between different users and computers. When you build your image, you can either run it on the computer you’ve built it on, or you can push (upload) the image to a registry and then pull (download) it on another computer and run it there. Certain registries are public, allowing anyone to pull images from it, while others are private, only accessible to certain people or machines.

Containers :- A Docker-based container is a regular Linux container created from a Docker-based container image. A running container is a process running on the host running Docker, but it’s completely isolated from both the host and all other processes running on it. The process is also resource-constrained, meaning it can only access and use the number of resources (CPU, RAM, and so on) that are allocated to it.

![Docker-flow](./readme/docker-flow.png)

### Learning Resource


## Kubernetes




### What is Kubernetes


### Hardware level concept

### Software level concept


## Software level practical

#### Ex-1: Simple deployment sample

#### Ex-2: containers comunication between deployment

#### Ex-3: Deployment with multiple Containers in a pod

#### Ex-4:

