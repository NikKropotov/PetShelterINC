ymaps.ready(init);

function init() {
    var myMap = new ymaps.Map('map', {
            center: [59.94, 30.32],
            zoom: 9,
        },
        {
            searchControlProvider: 'yandex#search'
        }),
        objectManager = new ymaps.ObjectManager({
            clusterize: true,
            gridSize: 32,
            clusterDisableClickZoom: true
        });
    objectManager.objects.options.set('preset', 'islands#greenDotIcon');
    objectManager.clusters.options.set('preset', 'islands#greenClusterIcons');
    myMap.geoObjects.add(objectManager);

    $.ajax({
        url: ('data.json')
    }).done(function (data) {
        objectManager.add(data);
    });

}