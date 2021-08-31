<script>
    function generateMap() {
        mapImg = document.getElementById("map-img");
        mapImg.src = '';

        var request = new XMLHttpRequest();

        request.onreadystatechange = function() {
            if (request.readyState == 4 && request.status == 200) {
                result = JSON.parse(request.responseText);
                mapImg.src = 'data:image/svg+xml;utf8,' + result.map;
            } else {
                alert('Error: ' + request.status);
            }
    }
</script>

<div>
    <button onclick="generateMap()">Generate Map!</button>
    <img id="map-img"/>
</div>
