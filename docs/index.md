<script>
    function generateMap() {
        mapImg = document.getElementById("map-img");

        var request = new XMLHttpRequest();

        request.onreadystatechange = function() {
            if (request.readyState == 4 && request.status == 200) {
                result = JSON.parse(request.responseText);
                mapImg.src = 'data:image/svg+xml;utf8,' + result.map;
            } else {
                alert('Error: ' + request.status);
                mapImg.src = '';
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
