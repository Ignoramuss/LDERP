data = [
	{
		"disability": "dyslexia",
		"age_group": "<10",
		"gender": "male",
		"education": "10th",
		"image": "http://www.sweetwater.com/images/items/120/LPST5HTHDCH-medium.jpg?9782bd"
	},
	{
		// "make": "Gibson",
		// "model": "SG",
		// "type": "Electric",
		// "price": "$1,500",
    "disability": "abcdef",
		"age_group": "10-16",
		"gender": "female",
		"education": "10th",
		"image": "http://www.sweetwater.com/images/items/120/SGSEBCH-medium.jpg?e69cfe"
	}
];

var products = "";
var makes = "";
var models = "";
var types = "";

for (var i = 0; i < data.length; i++) {
	var make = data[i].make,
		model = data[i].model,
		type = data[i].type,
		price = data[i].price,
		rawPrice = price.replace("$",""),
		rawPrice = parseInt(rawPrice.replace(",","")),
		image = data[i].image;

	//create product cards
	products += "<div class='col-sm-4 product' data-make='"+make+"' data-model='"+model+"' data-type='"+type+"' data-price='"+rawPrice+"'><div class='product-inner text-center'><img src='"+image+"'><br />Make: "+make +"<br />Model: "+model+"<br />Type: "+type+"<br />Price: "+price+"</div></div>";

	//create dropdown of makes
	if (makes.indexOf("<option value='"+make+"'>"+make+"</option>") == -1) {
		makes += "<option value='"+make+"'>"+make+"</option>";
	}

	//create dropdown of models
	if (models.indexOf("<option value='"+model+"'>"+model+"</option>") == -1) {
		models += "<option value='"+model+"'>"+model+"</option>";
	}

	//create dropdown of types
	if (types.indexOf("<option value='"+type+"'>"+type+"</option>") == -1) {
		types += "<option value='"+type+"'>"+type+"</option>";
	}
}

$("#products").html(products);
$(".filter-make").append(makes);
$(".filter-model").append(models);
$(".filter-type").append(types);

var filtersObject = {};

//on filter change
$(".filter").on("change",function() {
	var filterName = $(this).data("filter"),
		filterVal = $(this).val();

	if (filterVal == "") {
		delete filtersObject[filterName];
	} else {
		filtersObject[filterName] = filterVal;
	}

	var filters = "";

	for (var key in filtersObject) {
	  	if (filtersObject.hasOwnProperty(key)) {
			filters += "[data-"+key+"='"+filtersObject[key]+"']";
	 	 }
	}

	if (filters == "") {
		$(".product").show();
	} else {
		$(".product").hide();
		$(".product").hide().filter(filters).show();
	}
});

//on search form submit
$("#search-form").submit(function(e) {
	e.preventDefault();
	var query = $("#search-form input").val().toLowerCase();

	$(".product").hide();
	$(".product").each(function() {
		var make = $(this).data("disability").toLowerCase(),
			model = $(this).data("age_group").toLowerCase(),
			type = $(this).data("gender").toLowerCase();

		if (make.indexOf(query) > -1 || model.indexOf(query) > -1 || type.indexOf(query) > -1) {
			$(this).show();
		}
	});
});
