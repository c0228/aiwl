function getCurrentTimestampFormatted() {
  const now = new Date();

  const year = now.getFullYear();
  const month = String(now.getMonth() + 1).padStart(2, '0'); // Months are 0-indexed
  const day = String(now.getDate()).padStart(2, '0');
  const hours = String(now.getHours()).padStart(2, '0');
  const minutes = String(now.getMinutes()).padStart(2, '0');
  const seconds = String(now.getSeconds()).padStart(2, '0');

  return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
}

function load_modal(id, heading, body){
  let content='<!-- The Modal -->';
    content+='<div class="modal" id="'+id+'-template">';
    content+='<div class="modal-dialog">';
    content+='<div class="modal-content">';
    content+='<!-- Modal Header -->';
    content+='<div class="modal-header">';
    content+='<h5 class="modal-title">'+heading+'</h5>';
    content+='<button type="button" class="btn-close" data-bs-dismiss="modal"></button>';
    content+='</div>';
    content+='<!-- Modal body -->';
    content+='<div class="modal-body">'+body+'</div>';
    content+='</div>';
    content+='</div>';
    content+='</div>';
  document.getElementById(id).innerHTML = content;
}
function open_modal(id){
  const modalEl = document.getElementById(id+'-template');
  const bsModal = new bootstrap.Modal(modalEl, {backdrop: 'static'});
  bsModal.show();
}

function api_executor(url, func){
 fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok ' + response.statusText);
    }
    return response.json(); // parse JSON response
  })
  .then(data => { 
	func(data);
  });
}

function load_select_options(id, label, data){
 let content = '<option value="">'+label+'</option>';
	for(let i=0;i<data.length;i++){
		content+='<option value="'+data[i]+'">'+data[i]+'</option>';
	}
	document.getElementById(id).innerHTML = content;
}

function load_countries_list(prefix){
 api_executor('http://localhost/apis/get/countries/list',(data)=>{
	load_select_options(prefix+'_country', 'Select your Country', data);
 });
}

function load_states_list(prefix){
 const country = document.getElementById(prefix+"_country").value;
 const status = (country.length>0)?'block':'none';
 document.getElementById(prefix+"_states_module").style.display = status;
 api_executor('http://localhost/apis/get/'+country+'/data',(data)=>{
	document.getElementById(prefix+"_mobile_index").innerHTML = data?.["tel_index"];
	load_select_options(prefix+'_state', 'Select your State', data?.["states"]);
 });
}

function load_visaType_list(prefix){
 const country = document.getElementById(prefix+"_country").value;
 document.getElementById(prefix+"_visaType_module").style.display = 'block';
 api_executor('http://localhost/apis/get/'+country+'/data',(data)=>{
	load_select_options(prefix+'_visaType', 'Select Visa Type', data?.["visa_types"]);
 });
}


function load_form_alert(id,type,data){
 let content='<div class="alert alert-'+type+' alert-dismissible">';
	content+='<button type="button" class="btn-close" data-bs-dismiss="alert"></button>';
	content+=data;
	content+='</div>';
 document.getElementById(id).innerHTML = content;
}
