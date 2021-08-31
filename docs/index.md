<style>
    .hidden {
        display: none;
    }
</style>

<script>
    function generateMap() {
        var mapImg = document.getElementById("map-img");
        var radius = document.getElementById("radius").value;
        var generateMapBtn = document.getElementById("generate-map-btn");
        var errorRetries = 0;
        MAX_RETRIES = 2;

        var request = new XMLHttpRequest();

        var makeRequest = function() {
            request.open('GET', url);
            request.send();
        }

        var onRequestError = function() {
            if (errorRetries < MAX_RETRIES) {
                makeRequest();
                errorRetries++;
            } else {
                alert("Error: Could not generate map. Please try again later.");
                mapImg.classList.add("hidden");
                generateMapBtn.disabled = false;
            }
        }

        var onRequestLoad = function() {
            result = JSON.parse(this.responseText);
            mapImg.src = 'data:image/svg+xml;base64,' + result.map;
            generateMapBtn.disabled = false;
        };

        var url = 'https://real-world-rpg-maps-staging.herokuapp.com/';
        var queryParams = {};
        if (radius !== '') {
            queryParams.radius = radius;
        }

        url += '?' + Object.keys(queryParams).map(key => encodeURL(key) + '=' + encodeURI(queryParams[key])).join('&');

        request.addEventListener('load', onRequestLoad);
        request.addEventListener('error', onRequestError);

        mapImg.classList.remove("hidden");
        mapImg.src = 'spinner.gif';
        generateMapBtn.disabled = true;

        makeRequest();
    }
</script>

<div>
    <div>
        <input type="number" id="radius" placeholder="Radius" />
    </div>
    <div>
        <button onclick="generateMap()" id="generate-map-btn">Generate Map!</button>
    </div>
    <div>
        <img id="map-img" class="hidden" />
    </div>
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
