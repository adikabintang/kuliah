# Setting up kubernetes
tutorial: https://kubecloud.io/setting-up-a-kubernetes-1-11-raspberry-pi-cluster-using-kubeadm-952bbda329c8

### Disable swap on Ubuntu
This Intel Fog Computing Reference uses Ubuntu.
How to disable swap: 
- https://docs.platform9.com/support/disabling-swap-kubernetes-node/ 
- https://unix.stackexchange.com/questions/224156/how-to-safely-turn-off-swap-permanently-and-reclaim-the-space-on-debian-jessie

### Don't forget to read and do this after "kubeadm init" on master

Do the following lines spitted by `kubeadm init`:
```
mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

You can now join any number of machines by running the following on each node
as root:

  kubeadm join IP_ADDRESS:6443 --token TOKEN --discovery-token-ca-cert-hash sha256:HASH
```

### How to leave node
on master:
```
kubectl drain node-name
kubectl delete node node-name
```
on the node:
```
sudo kubeadm reset
```

## How to label nodes
Tutorial: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/

For example, a node named `blackraspi` is about to be labeled `machinetype=raspi`. Command:
```
kubectl label node blackraspi machinetype=raspi
# to see the labels of the nodes
kubectl get nodes --show-labels
```

## Deployment
Command:
```
kubectl create -f deployment.yaml
```
### How to set where the pod lands with node label selector:
Example:
```yaml
spec:
  replicas: ...
  selector:
    matchLabels:
      app: ...
  template:
    metadata:
      labels:
        app: ...
    spec:
      nodeSelector: # see this for node selector
        machinetype: raspi
      containers:
      - name: ...
        image: ...
        ports:
        - containerPort: ...
```

