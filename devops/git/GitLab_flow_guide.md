# 基于GitLab的项目管理与协作流程

GitLab 是一个类似于 GitHub 的开源源码托管服务。它除了提供基于 git 的基本代码托管服务外，还具备很多与软件开发协作相关的其他功能，比如 issues、Merge Requests 等。利用GitLab提供的这些功能，使我们的工作更加具有效率。下面具体介绍。

## 使用Issues来管理需求与缺陷

GitLab issues 类似于“工单系统”，是一个发布项目相关信息的地方。项目的所有成员都可以创建新的 issue，其他成员可以在 issue 下进行相关的讨论。

### 录入Issues

在项目的开发过程中，我们会碰到很多新的需求、软件 bug 等。这些需求与 bug ，就是 issue 最大的来源，它们都可以作为 issue 录入到项目的 issues 中。

鼓励**项目成员**录入 issue，但是要保证每个issue的内容质量。下面示例建议参考采用。

**编写优秀的“需求” issue**

- 用一句话描述你的需求，并用它作为标题
- 这个需求是解决什么问题的？
- 这个需求对软件现有功能会造成什么影响？
- 这个需求应该实现什么样的功能？
- 这个需求是否依赖其他模块提供相关支持？
- [可选] 这个需求有哪些实现方式？
- [可选] 这些可选的实现方式分别有哪些优缺点？

**编写优秀的“bug" issue**

- 提供出现问题的软件版本号、操作系统环境等相关信息
- 提供能够稳定复现问题的相关步骤
- 描述期待行为与当前行为
- *[可选]*
  你对这个 bug 原因的相关分析

### 评审Issues

当 issue 被创建后，**项目的owner**对issue进行Review。对于不满足的issue，评论中说明情况，并关闭该issue；对于应该继续跟进的issue，那就应该打上标签，方便之后的筛选、排期等工作。

具体怎么有效的打标签，后面有时间具体介绍。

### 关闭Issues

随着项目越来越大，项目累积的 issue 也会越来越多，而这些 issue 中有很多已经失去它的价值。所以，为了避免有价值的 issue 淹没在这些过时的信息当中，我们应该定期 Review 现有的 issues，关闭掉那些已经过时的 issues。

## Merge Request 的开发流程

几点需要注意

* 所有人都不应该直接往 master 分支推送代码
* 其他分支（或者fork项目的分支）进行开发
* 通过创建MergeRequest将代码合并到master分支

![img](C:\Users\cheng.lu\AppData\Local\Temp\企业微信截图_15666280438763.png)

### 创建Merge Request进行Code Review

需求或Bug都是用Issue来表示

任务的接收者对Issue创建Merge Request

完成任务后推送代码到Merge Request对应的分支

管理员对代码进行Merge



## Development Workflow

1. Fork

2. Clone fork to local storage

   git clone <remote your clone repo url>

   git remote add upstream <remote original repo url>

   \# Never push to upstream master

   git remote set-url --push upstream no_push

3. Keep your branch in sync

   git fetch upstream

   git checkout master

   git rebase upstream/master

4. Add new features

   git checkout –b myfeature

   \#edit code on the feature branch

    \# Rebase your the master branch of your local repo

   git checkout master

   git rebase upstream/master

​		\# make your development branch in sync with master branch

​		git checkout myfeature

​		git rebase -i master

5. Push to your folk

   git push –f <remote your clone repo url> myfeature