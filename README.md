# 销售转化看板 · Sales Conversion Dashboard

一个零依赖的数据看板网站：KPI 卡、转化漏斗、双轴趋势图、渠道对比与明细表，全部用原生 Canvas 绘制，不需要任何图表库或付费 API。

## 本地查看

双击 `index.html` 即可，或：

```bash
python -m http.server 8000
```

## 修改数据

打开 `index.html`，找到顶部 `DATA` 对象：

```js
const DATA = {
  channels: [
    { name:"自然搜索", visitors:18420, leads:2260, deals:312, prevDeals:286 },
    ...
  ],
};
```

- `visitors` 访客数 · `leads` 线索数 · `deals` 成交数 · `prevDeals` 上期成交（用于环比）
- 增删渠道会自动同步到柱状图、明细表与 KPI 汇总
- 趋势图的每日波动由 `makeSeries()` 按渠道总量生成；接入真实日数据时，替换该函数返回 `{vis, conv}` 数组即可

所有数字均为演示数据，页面顶部有 `DEMO DATA` 标注，接入真实数据后可删除该标签。

## 部署

推到 GitHub 后由 GitHub Pages 托管：

```bash
git add -A && git commit -m "update" && git push
```

线上地址：https://qian0729.github.io
