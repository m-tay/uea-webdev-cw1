var openPhotoSwipe = function() {
    var pswpElement = document.querySelectorAll('.pswp')[0];

    // build items array
    var items = [
        {
            src: 'static/gallery/img/hotel1.jpg',
            w: 1920,
            h: 1200
        },
        {
            src: 'static/gallery/img/hotel2.jpg',
            w: 1400,
            h: 900
        },
        {
            src: 'static/gallery/img/hotel3.jpg',
            w: 1650,
            h: 900
        },
        {
            src: 'static/gallery/img/hotel4.jpg',
            w: 1600,
            h: 800
        },
        {
            src: 'static/gallery/img/hotel5.jpg',
            w: 1320,
            h: 742
        },
        {
            src: 'static/gallery/img/hotel6.jpg',
            w: 1030,
            h: 686
        },
        {
            src: 'static/gallery/img/hotel7.jpg',
            w: 2095,
            h: 984
        },
    ];
    
    // define options (if needed)
    var options = {
             // history & focus options are disabled on CodePen        
        history: false,
        focus: false,

        showAnimationDuration: 0,
        hideAnimationDuration: 0
        
    };
    
    var gallery = new PhotoSwipe( pswpElement, PhotoSwipeUI_Default, items, options);
    gallery.init();
};

openPhotoSwipe();

document.getElementById('btn').onclick = openPhotoSwipe;