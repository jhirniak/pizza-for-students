function callWikipediaAPI(wikipediaPage, callback) {    
    $.getJSON('http://en.wikipedia.org/w/api.php?action=parse&format=json&callback=?', {page:wikipediaPage, prop:'text|images', uselang:'en'}, function(data) {

    var readData = $('<div>' + data.parse.text["*"] + '</div>');
    //handle redirects

    var redirect = readData.find('li:contains("REDIRECT") a').text();
    if(redirect != '') {
    	callWikipediaAPI(redirect);
        return;
    }
    
    var box = readData.find('.infobox');
    
    //var binomialName    = box.find('.binomial').text();
    //var fishName        = box.find('th').first().text();
    var imageURL        = null;
 
    // Check if page has images
    if(data.parse.images.length >= 1) {
        imageURL = box.find('img').first().attr('src');
    }
    
    //imageURL = JSON.stringify(imageURL);
    //document.write(imageURL.substring(7));
    //callback(imageURL);
    //$('#insertTest').append('<div><img src="'+ imageURL + '"/></div>');
    callback(imageURL);
});
}
