const CREATE_PROFILE_DATA = {
 profileId: PROFILE_ID,
 personalDetails:{},
 eduDetails:[],
 empDetails:[],
 visaDetails:{},
 techStackDetails:{},
 createdOn: '',
 updatedOn: ''
};

/* ----- ON PAGE LOAD ::: START --------------------------------------------------------*/
$(document).ready(function(){
    load_countries_list('createProfile_personalDetails');
    load_createProfile_leftMenu('createProfile_leftMenu', 'personal_details');
});

/* ------ PERSONAL DETAILS ::: START ----------------------------------------------- */
const LOAD_CREATEPROFILE_LEFTMENUDATA = [{
    id: "personal_details",
    name: "Personal Details",
    view: "createProfile_formDisplay_personalDetails"
 },{
    id: "edu_qualifications",
    name: "Educational Qualifications",
    view: "createProfile_formDisplay_eduDetails"
 },{
    id: "emp_details",
    name: "Employer's Details",
    view: "createProfile_formDisplay_empDetails"
 },{
    id: "visa_details",
    name: "Visa Details",
    view: "createProfile_formDisplay_visaDetails"
 },{
    id: "tech_stack_details",
    name: "Tech Stack Details",
    view: "createProfile_formDisplay_techStackDetails"
 }];
function sel_createProfile_leftMenu(activeId){
 for(let i=0;i<LOAD_CREATEPROFILE_LEFTMENUDATA?.length;i++){
    const menuId = LOAD_CREATEPROFILE_LEFTMENUDATA[i]?.id;
    const view = LOAD_CREATEPROFILE_LEFTMENUDATA[i]?.view;
    if(activeId===menuId){
        $('#'+menuId).removeClass('disabled');
        $('#'+menuId).addClass('active fWBold');
        document.getElementById(view).style.display='block';
    } else {
        $('#'+menuId).removeClass('active fWBold');
        $('#'+menuId).addClass('disabled');
        document.getElementById(view).style.display='none';
    }
 }
}
function load_createProfile_leftMenu(id, activeId) {
 let menuView;
 let content='<ul class="nav nav-pills flex-column">';
    for(let i=0;i<LOAD_CREATEPROFILE_LEFTMENUDATA?.length;i++){
        const menuId = LOAD_CREATEPROFILE_LEFTMENUDATA[i]?.id;
        const menuName = LOAD_CREATEPROFILE_LEFTMENUDATA[i]?.name;
        content+='<li class="nav-item">';
        if(activeId===menuId) {
            menuView = LOAD_CREATEPROFILE_LEFTMENUDATA[i]?.view;
            content+='<a id="'+menuId+'" class="nav-link active fWBold" href="#">'+menuName+'</a>';
        } else {
            content+='<a id="'+menuId+'" class="nav-link disabled" href="#">'+menuName+'</a>';
        }
        content+='</li>';
    }
    content+='</ul>';
 document.getElementById(id).innerHTML = content;
 document.getElementById(menuView).style.display='block';
}
function save_createProfile_personalDetails(){
 // Data Validation and Saving into File in data Folder by Unlocking by giving data to Backend
 const name = document.getElementById("createProfile_personalDetails_name").value;
 const email = document.getElementById("createProfile_personalDetails_email").value;
 const country = document.getElementById("createProfile_personalDetails_country").value;
 const state = document.getElementById("createProfile_personalDetails_state").value;
 const mobileIndex = document.getElementById("createProfile_personalDetails_mobile_index").textContent;
 const mobile = document.getElementById("createProfile_personalDetails_mobile").value;

 if(name?.length>0 && email?.length>0 && country?.length>0 && state?.length>0 && mobileIndex?.length>0 && 
   mobile?.length>0){
      $('#createProfile_personalDetails_name').addClass('valid-form');
      $('#createProfile_personalDetails_email').addClass('valid-form');
      $('#createProfile_personalDetails_country').addClass('valid-form');
      $('#createProfile_personalDetails_state').addClass('valid-form');
      $('#createProfile_personalDetails_mobile_index').addClass('valid-form');
      $('#createProfile_personalDetails_mobile').addClass('valid-form');

      CREATE_PROFILE_DATA["personalDetails"].name = name;
      CREATE_PROFILE_DATA["personalDetails"].email = email;
      CREATE_PROFILE_DATA["personalDetails"].country = country;
      CREATE_PROFILE_DATA["personalDetails"].state = state;
      CREATE_PROFILE_DATA["personalDetails"].mobile = mobileIndex+'-'+mobile;
      console.log("CREATE_PROFILE_DATA", CREATE_PROFILE_DATA);

      load_form_alert('createProfiles_form_alert', 'success', '<strong>Success!</strong> Your Personal Details got saved Successfully');
      document.getElementById("createProfile_formNextBtn_personalDetails").style.display='inline-block';

 } else {
      let missingData='Missing';

      if(name?.length === 0) { $('#createProfile_personalDetails_name').addClass('invalid-form');missingData+=' Name /'; }
      else { $('#createProfile_personalDetails_name').addClass('valid-form'); }

      if(email?.length === 0) { $('#createProfile_personalDetails_email').addClass('invalid-form');missingData+=' Email /'; }
      else { $('#createProfile_personalDetails_email').addClass('valid-form'); }

      if(country?.length === 0) { $('#createProfile_personalDetails_country').addClass('invalid-form');missingData+=' Country /'; }
      else {
         $('#createProfile_personalDetails_country').addClass('valid-form');
         if(state?.length === 0) { $('#createProfile_personalDetails_state').addClass('invalid-form');missingData+=' State /'; }
         else { $('#createProfile_personalDetails_state').addClass('valid-form'); }
         if(mobile?.length === 0) { 
            $('#createProfile_personalDetails_mobile_index').addClass('invalid-form');
            $('#createProfile_personalDetails_mobile').addClass('invalid-form');
            missingData+=' Mobile Number /'; 
         } else {
            $('#createProfile_personalDetails_mobile_index').addClass('valid-form');
            $('#createProfile_personalDetails_mobile').addClass('valid-form');
         }
      }

      load_form_alert('createProfiles_form_alert', 'danger', '<strong>Error!</strong> '+missingData.substring(0,missingData.length-1).trim());
      document.getElementById("createProfile_formNextBtn_personalDetails").style.display='none';
 }
}
function next_createProfile_personalDetails(){
 sel_createProfile_leftMenu('edu_qualifications');
  loadUI_new_educationQualification('academic-record-1');
}
/* ------ PERSONAL DETAILS ::: END ----------------------------------------------- */
/* ------ EDUCATIONAL QUALIFICATIONS ::: START ----------------------------------- */
function previous_createProfile_eduDetails(){
 sel_createProfile_leftMenu('personal_details');
 document.getElementById("createProfile_formNextBtn_personalDetails").style.display='none';
}
function save_createProfile_eduDetails(){
 document.getElementById("createProfile_formNextBtn_eduDetails").style.display='inline-block';
 // Data Validation and Saving into File in data Folder by Unlocking by giving data to Backend
 // ACADEMIC_RECORD_INDEX
}
function next_createProfile_eduDetails(){
 sel_createProfile_leftMenu('emp_details');
 loadUI_new_employerDetails('employers-record-1');
}
function loadUI_edu_courseName(index){
 let content='<div class="col-md-4">';
    content+='<!-- Degree & Major -->';
    content+='<div class="mb-3 mt-3">';
    content+='<div for="createProfile_eduDetails_courseName'+index+'" class="form-label">';
    content+='<b>Course:</b>';
    content+='<span class="font-red fs12 mt3p float-end"><i>[Required Field]</i></span>';
    content+='</div>';
    content+='<input type="text" class="form-control" id="createProfile_eduDetails_courseName'+index+'" ';
    content+='placeholder="e.g. B.Tech in Computer Science & Engineering">';
    content+='</div>';
    content+='</div><!--/.col-md-4 -->';
 return content;
}
function loadUI_edu_schoolCollegeName(index){
 let content='<div class="col-md-4">';
    content+='<!-- University / College Name -->';
    content+='<div class="mb-3 mt-3">';
    content+='<div for="createProfile_eduDetails_collegeName'+index+'" class="form-label">';
    content+='<b>School / College Name:</b>';
    content+='<span class="font-red fs12 mt3p float-end"><i>[Required Field]</i></span>';
    content+='</div>';
    content+='<input type="text" class="form-control" id="createProfile_eduDetails_collegeName'+index+'" ';
    content+=' placeholder="e.g. Jawaharlal Nehru Technological University, Hyderabad">';
    content+='</div>';
    content+='</div><!--/.col-md-4 -->';
 return content;
}
function loadUI_edu_location(index){
 let content='<div class="col-md-4">';
    content+='<!-- Location -->';
    content+='<div class="mb-3 mt-3">';
    content+='<div for="createProfile_eduDetails_location'+index+'" class="form-label">';
    content+='<b>Location:</b>';
    content+='<span class="font-red fs12 mt3p float-end"><i>[Required Field]</i></span>';
    content+='</div>';
    content+='<input type="text" class="form-control" id="createProfile_eduDetails_location'+index+'" ';
    content+=' placeholder="e.g. Hyderabad">';
    content+='</div>';
    content+='</div><!--/.col-md-4 -->';
 return content;
}
function loadUI_edu_country(index){
 let content='<div class="col-md-4">';
    content+='<!-- Location -->';
    content+='<div class="mb-3 mt-3">';
    content+='<div for="createProfile_eduDetails_country'+index+'" class="form-label">';
    content+='<b>Country:</b>';
    content+='<span class="font-red fs12 mt3p float-end"><i>[Required Field]</i></span>';
    content+='</div>';
    content+='<input type="text" class="form-control" id="createProfile_eduDetails_country'+index+'" ';
    content+=' placeholder="e.g. India">';
    content+='</div>';
    content+='</div><!--/.col-md-4 -->';
 return content;
}
function loadUI_edu_yearsOfPassing(index){
 let content='<div class="col-md-4">';
    content+='<!-- Year of Passing -->';
    content+='<div class="mb-3 mt-3">';
    content+='<div for="createProfile_eduDetails_yearOfPassing'+index+'" class="form-label">';
    content+='<b>Year of Passing:</b>';
    content+='<span class="font-red fs12 mt3p float-end"><i>[Required Field]</i></span>';
    content+='</div>';
    content+='<div class="row">';
    content+='<div class="col">';
    content+='<input type="text" class="form-control" id="createProfile_eduDetails_yearOfPassing'+index+'_from" placeholder="From (e.g. 2010)">';
    content+='</div>';
    content+='<div class="col">';
    content+='<input type="text" class="form-control" id="createProfile_eduDetails_yearOfPassing'+index+'_to" placeholder="To (e.g. 2014)">';
    content+='</div>';
    content+='</div>';
    content+='</div>';
    content+='</div><!--/.col-md-4 -->';
 return content;
}
function loadUI_percentageCGPA(index){
 let content='<div class="col-md-4">';
    content+='<!-- Percentage / CGPA -->';
    content+='<div class="mb-3 mt-3">';
    content+='<div for="createProfile_eduDetails_percentage'+index+'" class="form-label">';
    content+='<b>Percentage / CGPA:</b>';
    content+='<span class="font-gray fs12 mt3p float-end"><i>[Optional]</i></span>';
    content+='</div>';
    content+='<input type="text" class="form-control" id="createProfile_eduDetails_percentage'+index+'" ';
    content+='placeholder="e.g. 8.1/10 or 78%">';
    content+='</div>';
    content+='</div><!--/.col-md-4 -->';
 return content;
}
function loadUI_edu_relevantAchievement(index) {
 let content='<div class="col-md-12">';
    content+='<!-- Relevant Achievements -->';
    content+='<div class="mb-3 mt-3">';
    content+='<div for="createProfile_eduDetails_achievements'+index+'" class="form-label">';
    content+='<b>Relevant Achievements:</b>';
    content+='<span class="font-gray fs12 mt3p float-end"><i>[Optional]</i></span>';
    content+='</div>';
    content+='<textarea class="form-control" id="createProfile_eduDetails_achievements'+index+'" rows="4" ';
    content+='placeholder="e.g. Top 5% of class, Gold Medalist"></textarea>';
    content+='</div>';
    content+='</div><!--/.col-md-12 -->';
 return content;
}
let ACADEMIC_RECORD_INDEX = 1;
function loadUI_new_educationQualification(id) {
 let content='<div>';
    content+='<div class="mt-3" style="border:2px dashed #ccc;padding:15px;">';
    content+='<!-- -->';
    content+='<div class="row">';
    content+='<div class="col-md-12">';
    content+='<h5>ACADEMIC RECORD #'+ACADEMIC_RECORD_INDEX;
    if(ACADEMIC_RECORD_INDEX>1){
    content+='<span class="float-end curpoint">';
    content+='<i class="fa fa-minus-circle" aria-hidden="true" ';
    content+='onclick="javascript:form_confirmDelete_educationQualification('+ACADEMIC_RECORD_INDEX+');"></i>';
    content+='</span>';
    }
    content+='</h5><hr/>';
    content+='</div><!--/.col-md-12 -->';
    content+='</div><!--/.row -->';
    content+='<div class="row">';
    content+=loadUI_edu_courseName(ACADEMIC_RECORD_INDEX);
    content+=loadUI_edu_schoolCollegeName(ACADEMIC_RECORD_INDEX);
    content+=loadUI_edu_location(ACADEMIC_RECORD_INDEX);
    content+='</div><!--/.row -->';
    content+='<div class="row">';
    content+=loadUI_edu_country(ACADEMIC_RECORD_INDEX);
    content+=loadUI_edu_yearsOfPassing(ACADEMIC_RECORD_INDEX);
    content+=loadUI_percentageCGPA(ACADEMIC_RECORD_INDEX);
    content+='</div><!--/.row -->';
    content+='<div class="row">';
    content+=loadUI_edu_relevantAchievement(ACADEMIC_RECORD_INDEX);
    content+='</div><!--/.row -->';
    content+='</div>';
    content+='</div>';
    // content+='<div id="academic-record-'+(ACADEMIC_RECORD_INDEX+1)+'"></div>';
 document.getElementById(id).innerHTML = content;
 const newRecord = document.createElement('div');
    newRecord.id = 'academic-record-' + (ACADEMIC_RECORD_INDEX+1);
 const container = document.getElementById('academic-records');
    container.appendChild(newRecord);
}
function form_addNew_educationQualification(){
 ACADEMIC_RECORD_INDEX++;
 loadUI_new_educationQualification('academic-record-'+ACADEMIC_RECORD_INDEX);
}
function form_confirmDelete_educationQualification(index){
 const modalId = 'createProfile-display-modal';
 const heading = 'Delete Notification';
 let body='<div align="center" >';
    body+='<div><b>Are you sure to delete this ACADEMIC RECORD #'+index+'?</b></div>';
    body+='<div class="mt-2 btn-group btn-group-sm">';
    body+='<button type="button" class="btn btn-success" ';
    body+='onclick="javascript:form_remove_educationQualification('+index+');">Yes</button>';
    body+='<button type="button" class="btn btn-danger">No</button>';
    body+='</div>';
 load_modal(modalId, heading, body);
 open_modal(modalId);
}
function form_remove_educationQualification(index){
  console.log('academic-record-'+index);
  document.getElementById('academic-record-'+index).innerHTML = '';
}
/* ------ EDUCATIONAL QUALIFICATIONS ::: END ----------------------------------- */
/* ------ EMPLOYEE'S DETAILS ::: START ----------------------------------- */
function previous_createProfile_empDetails(){
 sel_createProfile_leftMenu('edu_qualifications');
 document.getElementById("createProfile_formNextBtn_eduDetails").style.display='none';
}
function save_createProfile_empDetails(){
 document.getElementById("createProfile_formNextBtn_empDetails").style.display='inline-block';
 // Data Validation and Saving into File in data Folder by Unlocking by giving data to Backend
 // EMPLOYER_RECORD_INDEX
}
function next_createProfile_empDetails(){
 sel_createProfile_leftMenu('visa_details');
 load_countries_list("createProfiles_visaWorkAuth");
}
function loadUI_emp_companyName(index){
 let content='<div class="col-md-6">';
    content+='<!-- -->';
    content+='<div id="createProfiles_form_alert" class="mb-3"></div>';
    content+='<div class="mb-3">';
    content+='<div for="createProfile_empDetails_companyName'+index+'" class="form-label"><b>Company Name:</b>';
    content+='<span class="font-red fs12 mt3p float-end"><i>[Required Field]</i></span>';
    content+='</div>';
    content+='<input type="text" class="form-control" id="createProfile_empDetails_companyName'+index+'" ';
    content+='placeholder="Enter Company Name">';
    content+='</div>';
    content+='<!-- -->';
    content+='</div><!--/.col-md-6 -->';
 return content;
}
function loadUI_emp_location(index){
 let content='<div class="col-md-3">';
    content+='<!-- -->';
    content+='<div class="mb-3">';
    content+='<div for="createProfile_empDetails_location'+index+'" class="form-label"><b>Location:</b>';
    content+='<span class="font-red fs12 mt3p float-end"><i>[Required Field]</i></span>';
    content+='</div>';
    content+='<input type="text" class="form-control" id="createProfile_empDetails_location'+index+'" ';
    content+='placeholder="Enter Location">';
    content+='</div>';
    content+='<!-- -->';
    content+='</div><!--/.col-md-3 -->';
 return content;
}
function loadUI_emp_country(index){
 let content='<div class="col-md-3">';
    content+='<!-- -->';
    content+='<div class="mb-3">';
    content+='<div for="createProfile_empDetails_country'+index+'" class="form-label"><b>Country:</b>';
    content+='<span class="font-red fs12 mt3p float-end"><i>[Required Field]</i></span>';
    content+='</div>';
    content+='<input type="text" class="form-control" id="createProfile_empDetails_country'+index+'" ';
    content+='placeholder="Enter Country">';
    content+='</div>';
    content+='<!-- -->';
    content+='</div><!--/.col-md-3 -->';
 return content;
}
function loadUI_emp_jobTitle(index){
 let content='<div class="col-md-6">';
    content+='<!-- -->';
    content+='<div id="createProfiles_form_alert" class="mb-3 mt-3"></div>';
    content+='<div class="mb-3 mt-3">';
    content+='<div for="createProfile_empDetails_jobTitleRole'+index+'" class="form-label"><b>Job Title / Role:</b>';
    content+='<span class="font-red fs12 mt3p float-end"><i>[Required Field]</i></span>';
    content+='</div>';
    content+='<input type="text" class="form-control" id="createProfile_empDetails_jobTitleRole'+index+'" ';
    content+='placeholder="Enter Job Title / Role">';
    content+='</div>';
    content+='<!-- -->';
    content+='</div><!--/.col-md-6 -->';
 return content;
}
function loadUI_emp_from(index){
 let content='<div class="col-md-3">';
    content+='<!-- -->';
    content+='<div class="mb-3 mt-3">';
    content+='<div for="createProfile_empDetails_from'+index+'" class="form-label"><b>From:</b>';
    content+='<span class="font-red fs12 mt3p float-end"><i>[Required Field]</i></span>';
    content+='</div>';
    content+='<input type="date" class="form-control" id="createProfile_empDetails_from'+index+'" placeholder="Enter From">';
    content+='</div>';
    content+='<!-- -->';
    content+='</div><!--/.col-md-3 -->';
 return content;
}
function loadUI_emp_to(index){
  let content='<div class="col-md-3">';
    content+='<!-- -->';
    content+='<div class="mb-3 mt-3">';
    content+='<div for="createProfile_empDetails_to'+index+'" class="form-label"><b>To:</b>';
    content+='<span class="font-red fs12 mt3p float-end"><i>[Required Field]</i></span>';
    content+='</div>';
    content+='<input type="date" class="form-control" id="createProfile_empDetails_to'+index+'" placeholder="Enter To">';
    content+='</div>';
    content+='<!-- -->';
    content+='</div><!--/.col-md-3 -->';
 return content;
}
function loadUI_emp_currentWorking(index){
 let content='<div class="col-md-3">';
    content+='<!-- -->';
    content+='<div class="mb-3 mt-3">';
    content+='<div class="form-check">';
    content+='<input class="form-check-input" type="checkbox" id="createProfile_empDetails_currentWorking'+index+'" ';
    content+='style="width:25px;height:25px;cursor:pointer;">';
    content+='<label class="form-check-label" for="createProfile_empDetails_currentWorking'+index+'" ';
    content+='style="padding-top:5px;padding-left:5px;">Currently Working</label>';
    content+='</div>';
    content+='</div>';
    content+='<!--/.col-md-3 -->';
    content+='</div>';
 return content;
}
function loadUI_emp_responsibilities(index){
 let content='<div class="col-md-12">';
    content+='<!-- -->';
    content+='<div class="mb-3 mt-3">';
    content+='<label for="createProfile_empDetails_responsibilities'+index+'" class="form-label"><b>Key Responsibilities</b></label>';
    content+='<textarea class="form-control" id="createProfile_empDetails_responsibilities'+index+'" rows="4" ';
    content+='placeholder="List major tasks and responsibilities"></textarea>';
    content+='</div>';
    content+='<!-- -->';
    content+='</div><!--/.col-md-12 -->';
 return content;
}
function loadUI_emp_achievements(index){
 let content='<div class="col-md-12">';
    content+='<!-- -->';
    content+='<div class="mb-3 mt-3">';
    content+='<label for="createProfile_empDetails_achievements'+index+'" class="form-label"><b>Key Achievements</b></label>';
    content+='<textarea class="form-control" id="createProfile_empDetails_achievements'+index+'" rows="4" ';
    content+='placeholder="e.g. Improved API response time by 40%"></textarea>';
    content+='</div>';
    content+='<!-- -->';
    content+='</div><!--/.col-md-12 -->';
 return content;
}
function load_emp_techStack(index){
 let content='<div class="col-md-12">';
    content+='<!-- -->';
    content+='<div class="mb-3 mt-3">';
    content+='<label for="createProfile_empDetails_techStack'+index+'" class="form-label"><b>Tech Stack / Tools</b></label>';
    content+='<textarea type="text" class="form-control" id="createProfile_empDetails_techStack'+index+'" rows="4" ';
    content+='placeholder="e.g. React, Node.js, AWS, Docker"></textarea>';
    content+='</div>';
    content+='<!-- -->';
    content+='</div><!--/.col-md-12 -->';
 return content;
}
let EMPLOYER_RECORD_INDEX = 1;
function loadUI_new_employerDetails(id){
 let content='<div class="mt-3" style="border:2px dashed #ccc;padding:15px;">';
    content+='<div class="row">';
    content+='<div class="col-md-12">';
    content+='<h5>EMPLOYER RECORD #'+EMPLOYER_RECORD_INDEX;
    if(EMPLOYER_RECORD_INDEX>1){
    content+='<span class="float-end curpoint">';
    content+='<i class="fa fa-minus-circle" aria-hidden="true"></i>';
    content+='</span>';
    }
    content+='</h5><hr/>';
    content+='</div>';
    content+='</div>';
    content+='<div class="row">';
    content+=loadUI_emp_companyName(EMPLOYER_RECORD_INDEX);
    content+=loadUI_emp_location(EMPLOYER_RECORD_INDEX);
    content+=loadUI_emp_country(EMPLOYER_RECORD_INDEX);
    content+='</div><!--/.row -->';
    content+='<div class="row">';
    content+=loadUI_emp_jobTitle(EMPLOYER_RECORD_INDEX);
    content+=loadUI_emp_from(EMPLOYER_RECORD_INDEX);
    content+=loadUI_emp_to(EMPLOYER_RECORD_INDEX);
    content+='</div><!--/.row -->';
    content+='<div class="row">';
    content+=loadUI_emp_currentWorking(EMPLOYER_RECORD_INDEX);
    content+='</div><!--/.row -->';
    content+='<div class="row">';
    content+=loadUI_emp_responsibilities(EMPLOYER_RECORD_INDEX);
    content+='</div><!--/.row -->';
    content+='<div class="row">';
    content+=loadUI_emp_achievements(EMPLOYER_RECORD_INDEX);
    content+='</div><!--/.row -->';
    content+='<div class="row">';
    content+=load_emp_techStack(EMPLOYER_RECORD_INDEX);
    content+='</div><!--/.row -->';
    content+='</div>';
 document.getElementById(id).innerHTML = content;
 const newRecord = document.createElement('div');
    newRecord.id = 'employers-record-' + (EMPLOYER_RECORD_INDEX+1);
 const container = document.getElementById('employers-records');
    container.appendChild(newRecord);    
}
function form_addNew_employerDetails(){
 EMPLOYER_RECORD_INDEX++;
 loadUI_new_employerDetails('employers-record-'+EMPLOYER_RECORD_INDEX);
}
function form_confirmDelete_employerDetails(index){
 const modalId = 'createProfile-display-modal';
 const heading = 'Delete Notification';
 let body='<div align="center" >';
    body+='<div><b>Are you sure to delete this EMPLOYER\'s RECORD #'+index+'?</b></div>';
    body+='<div class="mt-2 btn-group btn-group-sm">';
    body+='<button type="button" class="btn btn-success" ';
    body+='onclick="javascript:form_remove_employerDetails('+index+');">Yes</button>';
    body+='<button type="button" class="btn btn-danger">No</button>';
    body+='</div>';
 load_modal(modalId, heading, body);
 open_modal(modalId);
}
function form_remove_employerDetails(index){
  console.log('employers-record-'+index);
  document.getElementById('employers-record-'+index).innerHTML = '';
}
/* ------ EMPLOYEE'S DETAILS ::: END ----------------------------------- */
/* ------ VISA DETAILS ::: START ----------------------------------- */
function previous_createProfile_visaDetails(){
 sel_createProfile_leftMenu('emp_details');
 document.getElementById("createProfile_formNextBtn_empDetails").style.display='none';
}
function save_createProfile_visaDetails(){
 document.getElementById("createProfile_formNextBtn_visaDetails").style.display='inline-block';
 // Data Validation and Saving into File in data Folder by Unlocking by giving data to Backend
}
function next_createProfile_visaDetails(){
 sel_createProfile_leftMenu('tech_stack_details');
}
/* ------ VISA DETAILS ::: END ----------------------------------- */
/* ------ TECH STACK DETAILS ::: START ----------------------------------- */
function previous_createProfile_techStackDetails(){
 sel_createProfile_leftMenu('visa_details');
 document.getElementById("createProfile_formNextBtn_visaDetails").style.display='none';
 document.getElementById("createProfile_formNextBtn_techStackDetails").style.display='none';
}
function save_createProfile_techStackDetails(){
 document.getElementById("createProfile_formNextBtn_techStackDetails").style.display='inline-block';
 // Data Validation and Saving into File in data Folder by Unlocking by giving data to Backend
}
function publish_createProfile_techStackDetails(){
 
}
/* ------ TECH STACK DETAILS ::: END ----------------------------------- */