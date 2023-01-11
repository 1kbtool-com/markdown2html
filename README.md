# markdown2html

使用 Python 构建的 markdown 转 html 小工具，附多种样式。

## 使用说明

实际上这个代码非常简单，不过可能考虑到不了解的朋友可能困惑于配置中出现的一些小问题，于是诞生了这个项目。

使用流程：

- 编写`README.md`。
- 运行`run.py`，在目录下生成`index.html`文件，用任意静态网页托管平台托管即可。

自定义样式：

默认使用 [Water.css](https://watercss.kognise.dev/) 样式，如需修改主题，可以更改`template.html`中`<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css@2/out/water.css">`为其他 classless css 包。以下列出几个可用包：

- [**Water.css**](https://watercss.kognise.dev/) - Just-add-CSS collection of styles to make simple websites just a little nicer.  
    [![](https://camo.githubusercontent.com/04297074b28037d454218d7d920c873406617d7ce32d9ff27364a8836886a405/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f6b6f676e6973652f77617465722e6373732e7376673f7374796c653d736f6369616c266c6162656c3d53746172)](https://camo.githubusercontent.com/04297074b28037d454218d7d920c873406617d7ce32d9ff27364a8836886a405/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f6b6f676e6973652f77617465722e6373732e7376673f7374796c653d736f6369616c266c6162656c3d53746172) [Repo](https://github.com/kognise/water.css) | #CSS
    
- [**MVP.css**](https://andybrewer.github.io/mvp/) - Minimalist stylesheet for HTML elements.  
    [![](https://camo.githubusercontent.com/91720bc4e541b8228538fc07e18f20f7bfbe834a768d942b44193532984f4335/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f616e64796272657765722f6d76702e7376673f7374796c653d736f6369616c266c6162656c3d53746172)](https://camo.githubusercontent.com/91720bc4e541b8228538fc07e18f20f7bfbe834a768d942b44193532984f4335/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f616e64796272657765722f6d76702e7376673f7374796c653d736f6369616c266c6162656c3d53746172) [Docs](https://andybrewer.github.io/mvp/#docs), [Repo](https://github.com/andybrewer/mvp/) | #CSS
    
- [**sakura**](https://oxal.org/projects/sakura/) - Minimal classless CSS framework/theme.  
    [![](https://camo.githubusercontent.com/4696645892a5a93c55f5c1724659918a77abc3d43d1e74effc55ea6c35b08a3d/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f6f78616c6f72672f73616b7572612e7376673f7374796c653d736f6369616c266c6162656c3d53746172)](https://camo.githubusercontent.com/4696645892a5a93c55f5c1724659918a77abc3d43d1e74effc55ea6c35b08a3d/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f6f78616c6f72672f73616b7572612e7376673f7374796c653d736f6369616c266c6162656c3d53746172) [Demo](https://oxal.org/projects/sakura/demo/), [Repo](https://github.com/oxalorg/sakura) | #SCSS
    
- [**Tacit**](https://yegor256.github.io/tacit/) - CSS framework for dummies, without classes.  
    [![](https://camo.githubusercontent.com/ed901fa523f0d91dd10433d468e15b5ba6ebe2f3174779af552ac8fd52934135/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f7965676f723235362f74616369742e7376673f7374796c653d736f6369616c266c6162656c3d53746172)](https://camo.githubusercontent.com/ed901fa523f0d91dd10433d468e15b5ba6ebe2f3174779af552ac8fd52934135/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f7965676f723235362f74616369742e7376673f7374796c653d736f6369616c266c6162656c3d53746172) [Repo](https://github.com/yegor256/tacit/) | #SCSS
    
- [**awsm.css**](https://igoradamenko.github.io/awsm.css/) - CSS library for semantic HTML markup without classes, attributes, etc.  
    [![](https://camo.githubusercontent.com/71d40465279056bcc373949af5690d2eb8c9984a7fbf28fca8c5585b5d00f9a3/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f69676f726164616d656e6b6f2f6177736d2e6373732e7376673f7374796c653d736f6369616c266c6162656c3d53746172)](https://camo.githubusercontent.com/71d40465279056bcc373949af5690d2eb8c9984a7fbf28fca8c5585b5d00f9a3/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f69676f726164616d656e6b6f2f6177736d2e6373732e7376673f7374796c653d736f6369616c266c6162656c3d53746172) [Demo](https://igoradamenko.github.io/awsm.css/elements.html), [Repo](https://github.com/igoradamenko/awsm.css) | #SCSS


一些其他资源（CSS）：

https://github.com/mixu/markdown-styles

https://github.com/mrcoles/markdown-css

https://github.com/picocss/pico