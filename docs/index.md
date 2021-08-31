<script>
    function generateMap() {
        mapImg = document.getElementById("map-img");

        var request = new XMLHttpRequest();

        request.onreadystatechange = function() {
            if (request.readyState == 4) {
                if (request.status == 200) {
                    result = JSON.parse(request.responseText);
                    mapImg.src = 'data:image/svg+xml;utf8,' + result.map;
                } else {
                    alert('Error: ' + request.status);
                    mapImg.src = '';
                }
            }
        };

        mapImg.src = 'spinner.gif';
        request.open('GET', 'https://real-world-rpg-maps-staging.herokuapp.com/');
    }
</script>

<div>
    <button onclick="generateMap()">Generate Map!</button>
    <img id="map-img"/>
</div>

<!--
## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/TheCleric/real-world-rpg-maps/edit/main/docs/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/TheCleric/real-world-rpg-maps/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
-->
