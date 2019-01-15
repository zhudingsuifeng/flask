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

每次提交，master分支都会向前移动一步，随着不断提交，master分支的线也越来越长。

创建新的dev分支，git新建了一个指针叫dev，指向master相同的提交，再把HEAD指向dev,就表示当前分支在dev上：

```
git checkout -b dev
Switched to a new branch 'dev'

# 相当于
git branch dev
git checkout dev
Switched to a new branch 'dev'

# 查看分支
git branch
* dev
  master
```

![dev](../imgs/git2.png)

后续对工作区的修改和提交就针对dev分支了，新提交一次后，dev指针往前移动一步，而master指针不变：

![dev commit](../imgs/git3.png)

在dev分支工作完成后，切换回master分支：

```
git checkout master
Switched to branch 'master'
```

![checkout](../imgs/git6.png)

合并dev分支的工作成果到master分支：

```
git merge dev
```

![merge](../imgs/git4.png)

git merge命令用于合并指定分支到当前分支。

合并完分支，可以删除dev分支，把dev指针删除掉后，就剩下master分支：

```
git branch -d dev
Deleted branch dev

# 删除远程分支
git push origin --delete works

git branch
* master
```

![delete brancd](../imgs/git5.png)

多人协作

```
# 创建本地分支和远程分支
git checkout -b dev origin/dev

# 指定本地dev分支与远程origin/dev分支的链接
git branch --set-upstream-to=origin/dev dev
Branch 'dev' set up to track remote branch 'dev' from 'origin'.

# 抓取远程分支与本地分支合并
git pull
```

多人协作的工作模式通常是：

1. 首先，可以试图用git push origin <branch-name>推送自己的修改；

2. 如果推送失败，则因为远程分支比你的本地分支更新，需要先用git pull试图合并；

3. 如果合并有冲突，则解决冲突，并在本地提交；

4. 么有冲突或者解决掉冲突后，再用git push origin <branch-name>推送；

如果git pull提示no tracking information,则说明本地分支和远程分支的链接关系没有创建，用命令git branch --set-upstream-to <branch-name> origin/<branch-name>创建分支链接。