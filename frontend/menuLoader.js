var mlParent,
    mlObjData,
    mlFirstDate,
    mlWidth;

var mlScriptNum = 4,
    mlScriptDone = 0;

function loadMenu(parent, object, firstDate, width)
{
    $.getScript("slider.js", mlLoaded);
    $.getScript("sliderContent.js", mlLoaded);
    $.getScript("menu.js", mlLoaded);
    $.getScript("table.js", mlLoaded);

    mlParent = parent;
    mlObjData = object;
    mlFirstDate = firstDate;
    mlWidth = width;
}

function mlLoaded() {
    mlScriptDone++;
    if (mlScriptDone == mlScriptNum) {
        createBar(mlParent, null, mlObjData, mlFirstDate, mlWidth);
    }
}

function mlTransformData(data) {


}