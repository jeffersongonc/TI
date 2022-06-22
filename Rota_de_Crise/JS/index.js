/* Learning about Google Maps API Services

* Explicações sobre Google Cloud API *
https://developers.google.com/learn/pathways/get-started-maps?authuser=2

* Documentação Google Maps API *
https://developers.google.com/maps/documentation/javascript
https://developers.google.com/maps/documentation/javascript/directions


DirectionsRequest{
	origin: LatLng | String | google.maps.Place, (Ponto de Origem)
		destination: LatLng | String | google.maps.Place, (Ponto de Destino)
		travelMode: TravelMode, (Modo da viagem: DRIVING (Default), BICYCLING, TRANSIT, WALKING)
		transitOptions: TransitOptions, (arrivalTime: Date (Optional) - departureTime: Date (Optional - Default Now) - 
										 modes[BUS, RAIL, SUBWAY, TRAIN, TRAM]: TransitMode (Optional) - 
										 routingPreference: TransitRoutePreference) (Optional) -
										 (FEWER_TRANSFERS (Limitar transferências na rota), LESS_WALKING (Limitar caminhada na rota))
		drivingOptions: DrivingOptions, (departureTime: Date (required) (How use: new Date(Date.now() + N)), 
										 trafficModel: TrafficModel Optional) ('bestguess' (default), 'pessimistic', 'optimistic'))
		unitSystem: UnitSystem, (.METRIC (Default in Long, Lat. KM), .IMPERIAL (Default in Places. MPH))
		waypoints[]: DirectionsWaypoint,
		optimizeWaypoints: Boolean,
		provideRouteAlternatives: Boolean,
		avoidFerries: Boolean,
		avoidHighways: Boolean,
		avoidTolls: Boolean,
		region: String
} 

* DirectionsStatus * may return the following values:

O DirectionsStatuspode retornar os seguintes valores:

OK - indica que a resposta contém um arquivo DirectionsResult.
NOT_FOUND - indica que pelo menos um dos locais especificados na origem, destino ou waypoints da solicitação não pôde ser geocodificado.
ZERO_RESULTS - indica que nenhuma rota foi encontrada entre a origem e o destino.
MAX_WAYPOINTS_EXCEEDED - indica que muitos DirectionsWaypointcampos foram fornecidos no arquivo DirectionsRequest. Consulte a seção abaixo sobre limites para pontos de passagem .
MAX_ROUTE_LENGTH_EXCEEDED - indica que a rota solicitada é muito longa e não pode ser processada. Este erro ocorre quando direções mais complexas são retornadas. Tente reduzir o número de waypoints, curvas ou instruções.
INVALID_REQUEST - indica que o fornecido DirectionsRequestera inválido. As causas mais comuns desse código de erro são solicitações sem origem ou destino ou uma solicitação de trânsito que inclui pontos de passagem.
OVER_QUERY_LIMIT - indica que a página da Web enviou muitas solicitações dentro do período permitido.
REQUEST_DENIED - indica que a página da Web não tem permissão para usar o serviço de rotas.
UNKNOWN_ERROR - indica que uma solicitação de rota não pôde ser processada devido a um erro do servidor. A solicitação pode ser bem-sucedida se você tentar novamente.
Você deve garantir que a consulta de rotas retornou resultados válidos verificando esse valor antes de processar o resultado.

* DirectionsResult * - contém o resultado da consulta de rotas, que você mesmo pode manipular ou passar para um 
					   DirectionsRenderer Para exibir um DirectionsResult usando um DirectionsRenderer, você 
					   precisa fazer o seguinte:

1. Crie um DirectionsRenderer objeto. 
	var directionsRenderer = new google.maps.DirectionsRenderer();
2. Chame setMap() o renderizador para vinculá-lo ao mapa passado.
	var map = new google.maps.Map(document.getElementById('map'), mapOptions);
		directionsRenderer.setMap(map);
3. Chame setDirections() o renderizador, passando-o DirectionsResult como indicado acima.
	directionsService.route(request, function(result, status) 
	{
		if (status == 'OK') 
		{
				directionsRenderer.setDirections(result);
		}
		});

* DirectionsRoute * - contém um único resultado da origem e destino especificados. Esta rota pode consistir 
					  em um ou mais trechos (do tipo DirectionsLeg) dependendo se algum waypoint foi especificado
*/
var map;
var directionsService = new google.maps.DirectionsService();
var info = new google.maps.InfoWindow({ maxWidth: 200 });
var myLatLng = { lat: -22.90748790474785, lng: -43.220902915341455 };
var myRoute = new Array();
var marker = new google.maps.Marker({
	/*title: 'Google Belo Horizonte',
	icon: 'marker.png',*/
	position: myLatLng
});

function initialize() {
	/*var myLatLng = { lat: -22.90748790474785, lng: -43.220902915341455 };*/
	var destLatLng = "Hospital Badim"/*{ lat: -22.914536912709146, lng: -43.23242524556165 }*/;
	var options = {
		zoom: 10,
		center: marker.position,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	};

	map = new google.maps.Map($('#map_content')[0], options);

	var trafficLayer = new google.maps.TrafficLayer();
	trafficLayer.setMap(map);

	new google.maps.Marker({
		position: myLatLng,
		map,
	});

	marker.setMap(map);

	google.maps.event.addListener(marker, 'click', function () {
		info.setContent($("#unidade").val());
		info.open(map, marker);
	});
	
}

function f_tempo() {
    //https://stackoverflow.com/questions/3251609/how-to-get-total-driving-distance-with-google-maps-api-v3
    var destLatLng2 = new Array("Hospital Badim",
                                "Hospital Glória D´Or",
                                "Hospital Norte D´Or",
                                "Hospital Rios D´Or",
                                "Hospital Niterói D´Or");
	var route;
	
	f_clearSelect('uni_destino');

	for (let i = 0; i < destLatLng2.length; i++) {
        var directionsDisplay = new google.maps.DirectionsRenderer();

        var request = {
            origin: $("#unidade").val(),
            destination: destLatLng2[i],
            travelMode: google.maps.DirectionsTravelMode.DRIVING
        };

        info.close();
        marker.setMap(null);

        directionsService.route(request, function (response, status) {
            if (status == google.maps.DirectionsStatus.OK) {
                directionsDisplay.setDirections(response);
                route = response.routes[0];
				f_addSelect('uni_destino', 
							route.legs[0].duration.text + " - " + destLatLng2[i] + " - " + route.legs[0].end_address, 
							destLatLng2[i]);
				
			}
        });
	}
	
	
	return false;
}

function f_tabela( vTab ) {
    document.getElementById("_resultado_tabela").appendChild(criarTabela([vTab]));
};


function f_addSelect (fElementID, fLabel, fValue){
	//Create OPTION in Select
	var vOption_Select = document.createElement("option");
	
	vOption_Select.value = fValue;
	
	//Create DESCRIPTION in Select
	var vDescription_Select = document.createTextNode(fLabel);
	
	vOption_Select.appendChild(vDescription_Select);
	
	//Create reference in HTML
	var vContainer_Select = document.getElementById(fElementID);

	vContainer_Select.appendChild(vOption_Select);
}

function f_clearSelect(fElementID){
	var vContainer_Select = document.getElementById(fElementID);

	while (vContainer_Select.length > 0) {
		vContainer_Select.remove(0);
	}
	f_addSelect("uni_destino", "Selecionar...", "blank");
}

function f_createRadio(fElementID, fLabel, fValue){
	//Create INPUT in Radio Button
	var vInput_Radio = document.createElement("input");
	
	vInput_Radio.type = 'radio';
	vInput_Radio.id = fValue;
	//vInput_Radio.onclick = f_Route(fValue);
	vInput_Radio.value = fValue;

	//Create LABEL in Radio Button
	var vLabel_Radio = document.createElement("label");

	vLabel_Radio.htmlFor = fValue;

	//Create DESCRIPTION in Radio Button
	var vDescription_Radio = document.createTextNode(" " + fLabel);
	vLabel_Radio.appendChild(vDescription_Radio);

	//Create LINE in Radio Button
	var vNewLine_Radio = document.createElement('br');

	//Create reference in HTML
	var vContainer_Radio = document.getElementById(fElementID);

	vContainer_Radio.appendChild(vInput_Radio);
	vContainer_Radio.appendChild(vLabel_Radio);
	vContainer_Radio.appendChild(vNewLine_Radio);

}
function criarTabela(vConteudo) {
    var tabela = document.createElement("table");
    var thead = document.createElement("thead");
    var tbody = document.createElement("tbody");
    var thd = function (i) { return (i == 0) ? "th" : "td"; };
    for (var i = 0; i < 1/*vConteudo.length*/; i++) {
        var tr = document.createElement("tr");
        for (var o = 0; o < vConteudo[i].length; o++) {
            var t = document.createElement(thd(i));
            var texto = document.createTextNode(vConteudo[i][o]);
            t.appendChild(texto);
            tr.appendChild(t);
        }
        (i == 0) ? thead.appendChild(tr) : tbody.appendChild(tr);
    }
    tabela.appendChild(thead);
    tabela.appendChild(tbody);
    return tabela;
};

function _Matrix (){
	var t_origin = new Array($("#unidade").val(), $("#unidade").val(), $("#unidade").val(), $("#unidade").val(), $("#unidade").val());
	var t_destination = new Array("Hospital Badim", "Hospital Glória D´Or", "Hospital Norte D´Or", "Hospital Rios D´Or", "Hospital Niterói D´Or");
	var service = new google.maps.DistanceMatrixService();
	var request_matrix = {
		origins: t_origin,
		destinations: t_destination,
		travelMode: 'DRIVING',
		//transitOptions: TransitOptions,
		drivingOptions: {departureTime: new Date(Date.now() + N), trafficModel: 'bestguess'},
		unitSystem: 'METRIC',
		avoidHighways: Boolean,
		avoidTolls: Boolean,
	};
	

	service.getDistanceMatrix( request_matrix, function (response, status) {
		console.log("0");
		if (status == 'OK') {
			var c_origins = response.originAddresses;
			var c_destinations = response.destinationAddresses;
				
			for (var i = 0; i < c_origins.length; i++) {
				var results = response.rows[i].elements;
				for (var j = 0; j < results.length; j++) {
					var element = results[j];
					var c_distance = element.distance.text;
					var c_duration = element.duration.text;
					var c_from = c_origins[i];
					var c_to = c_destinations[j];
					//alert(c_distance + c_duration + c_from + c_to);
				}
			}
		}
	});
}

function f_Direction (vOrigin, vDestiny, vReturn){
	let vRequest, vRoute, vResult, vRet_Start_Address, vRet_End_Address, vRet_Distance, vRet_Duration; 
	var vDirection = new google.maps.DirectionsRenderer();
	var vDS = new google.maps.DirectionsService();
	vResult = 'Vazio';
	
	vRequest = {
		origin: vOrigin,
		destination: vDestiny,
		travelMode: google.maps.DirectionsTravelMode.DRIVING
	};

	
	///////
	info.close();
    marker.setMap(null);

    directionsService.route(vRequest, function (response, status) {
        if (status == google.maps.DirectionsStatus.OK) {
            vDirection.setDirections(response);
            vRoute = response.routes[0];
			tabela(vRoute.legs[0].duration.text);
        }
    });
	
}

function f_Route ( ){
	
	initialize();
	info.close();
	marker.setMap(null);
	
	var f_RouteDirectiosDisplay = new google.maps.DirectionsRenderer();
		
	var request = {
		origin: $("#unidade").val(),
		destination: $("#uni_destino").val(),
		travelMode: google.maps.DirectionsTravelMode.DRIVING
	};

	directionsService.route(request, function (response, status) {
		if (status == google.maps.DirectionsStatus.OK) {
			f_RouteDirectiosDisplay.setDirections(response);
			f_RouteDirectiosDisplay.setRouteIndex(0);
			f_RouteDirectiosDisplay.setMap(map);
		}
	});
			
	return false;
}	
