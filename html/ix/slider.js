
var CONTENT_W = 0.9,
    CONTENT_H = 0.4,
    CONTENT_OFFSET = 0.05;

var SLIDER_OPACITY = 0.15,
    SLIDER_OPACITY_HOVER = 0.22;

var slider,
    sliderPanel,
    sliderPos = 0,
    sliderOffset = 3;       //TODO: PERCENT

function setupSlide() {
    sliderPanel = svg.append('g');
    slider = sliderPanel.append('rect')
        .attr('id', 'menuSelection')
        .attr('width', dayLength)
        .attr('height', barHeight)
                .attr('opacity', SLIDER_OPACITY)

        .on('mouseover', function (d, i) {
            d3.select(this).transition()
                .duration(150)
                .attr('opacity', SLIDER_OPACITY_HOVER)
        })
        .on('mouseout', function (d, i) {
        d3.select(this).transition()
            .duration(150)
            .attr('opacity', SLIDER_OPACITY)
        });


    setupContent();
}

//move the slider to another day
function moveSlider(id) {
    sliderPanel
        .transition().duration(TRANSITION_TIME)
        .attr("transform", "translate(" + (dayLength * id) + ",0.1)")
        .each('end', function () {
        });
    showContent(data[id], CONTENT_W * dayLength, CONTENT_H * barHeight);
}