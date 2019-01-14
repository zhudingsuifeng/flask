## git

### remote

```
# 为本地仓库关联远程仓库
git remote add origin git@github.com:zhudingsuifeng/flask.git

# 把当前分支master推送到远程，第一次推送时加上-u参数，git会推送分支，并和远程master分支关联
git push -u origin master 

# 后续推送就可以省略-u参数了
git push origin maste

# 推送当前分支到远程dev分支
git push origin dev

# 从远程克隆仓库到本地
git clone git@github.com:zhudingsuifeng/flask.git
```

### branch

创建个人分支，别人看不到，还继续在原来的分支上正常工作，而你在自己的分支上干活，随意提交，等开发完毕，一次性合并到原来的分支上，既安全又不影响别人工作。

多次提交串成一条时间线，这条时间线就是一个分支。

主分支即master分支。HEAD不指向提交，而是指向master，master才是指向提交，HEAD指向当前分支。

一开始的时候，master分支是一条线，Git用master指向最新的提交，再用HEAD指向master，就能确定当前分支，以及当前分支的提交点：

![init](../imgs/git1.png)

每次提交，master分支都会向前移动一步，随着你不断提交，master分支的线也越来越长：

<iframe height=270 width=360 src="../imgs/master-branch-forward.mp4">

```

```