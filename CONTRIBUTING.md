# 贡献指南

感谢关注 awesome-jev-apps！这份清单的目标是：**每一条都真实、可访问、值得点开**。投稿前请读完这份指南，多数问题都能在这里找到答案。

## 收录标准

1. **相关性**：与 Jev / TypeSafe AI / System One 决策模型直接相关（用它构建的项目、它的 SDK、它的深度评测）。
2. **可访问**：链接必须能打开。提交前请自己在浏览器里点一遍。
3. **优先级**：可运行的开源应用 > SDK / 集成 > 深度教程 > 社区讨论。
4. **不收录**：失效链接、纯营销落地页、搬运聚合号、无法核验的"据说很火"项目。

## 投稿方式

### 方式一：提 Issue（推荐给不想折腾 Git 的朋友）

用 [推荐新条目](https://github.com/JingHao-Leon/awesome-jev-apps/issues/new?template=submit-project.yml) 模板填写项目信息，维护者会处理入库。

### 方式二：直接提 PR

1. Fork 本仓库；
2. 在 `data/projects.json` 的对应分类下新增条目（字段见下）；
3. 在 `README.md` 的对应小节添加同一条目，格式统一为：

   ```markdown
   - [**名称**](URL) — 一句话中文描述（`语言`，★数快照）
   ```

4. 如果条目数变了，更新 README 开头的统计行；
5. 本地跑 `python scripts/check.py`，看到 `✓` 再提交；
6. 提 PR，模板里的清单逐项勾完。

### 条目数据格式（data/projects.json）

```json
{
  "name": "owner/repo 或站点名",
  "url": "https://…（必须 https）",
  "category": "优质开源应用 | SDK 与集成 | 官方资源 | 教程与评测 | 社区讨论",
  "subcategory": "小节名（官方资源 / 教程 / 讨论类填 null）",
  "language": "主语言（没有填 null）",
  "stars": "GitHub star 数（快照当日数值，非 GitHub 项目填 null）",
  "description": "一句话中文描述"
}
```

## 质检清单（PR 前自查）

- [ ] 链接浏览器实测可访问，落地内容与描述相符
- [ ] `data/projects.json` 与 `README.md` 已同步
- [ ] `python scripts/check.py` 通过
- [ ] 描述是自己的话，不是项目 README 的机翻
- [ ] star 数标注了快照日期（README 统计行的日期）

## 维护者会做什么

- 对每个 PR 做人工核验（点开链接、确认与 Jev 相关）；
- 每周由 CI 巡检一次全部链接，失效条目会开 Issue 跟踪；
- 不合标准的条目会说明原因后关闭，欢迎补充材料后重新提交。

## License

提交即表示同意你的贡献以 [MIT](LICENSE) 协议发布。
