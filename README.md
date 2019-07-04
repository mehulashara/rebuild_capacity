# rf

For calculating fault tolerance space usage threshold as reported by NCC:
1. Let G = Default gflag threshold for Stargate Read-Only mode.
2. Let T = Total storage capacity of the cluster
3. Let N1 = Total storage capacity of the largest storage node of the cluster (based on RF2)
Note: If the cluster is using RF3, let "N1" represent the total storage capacity of the two largest nodes in the cluster added together - (N1 + N2).
By design, Stargate stops allowing writes when the storage usage (T) reaches 95%. This percentage is the default setting. It is possible that the cluster has had this value modified during break/fix scenarios, but this is uncommon. If calculations using the below method do not seem to line up, contact Nutanix Support to investigate the current Stargate gflag setting.
The formula that NCC uses to calculate the threshold for "rebuild capacity" is as follows: 
