import React, { Component } from 'react';
import axios from 'axios';
import Zoom from 'react-reveal/Zoom';
import Flip from 'react-reveal/Flip';
import SubmissionForm from './submission_form/containers/SubmissionForm'

class App extends Component {
//   constructor() {
//     super();
//     this.state = {
//       data: [],
//     };
// }

// ClickPost(e){
//   e.preventDefault();
//   var url = 'http://localhost:3210/data';
//   axios.post(url, {
//     Name: this.inputname.value,
//     Breed: this.inputbreed.value,
//     Gender: this.inputgender.value,
//     Size: this.inputsize.value,
    
//   })
//   .then(function (response) {
//     console.log(response);
//   })
//   .catch(function (error) {
//     console.log(error);
//   });
//   this.inputname.value = '';
//   this.inputbreed.value = '';
//   this.inputgender.value = '';
//   this.inputsize.value = '';
// };

// ClickGet(e){
//   e.preventDefault();
//   var url = 'http://localhost:3210/data';
//   axios.get(url)
//   .then((RabbitData) => {
//     console.log(RabbitData.data);
//     this.setState({
//       data: RabbitData.data,
//     }) 
//   })
// };

render() {

  return (
    <div className="col-md-6">
      <h3> Sample Form Container </h3>
      <SubmissionForm/>
    </div>
  );
//   const dataMySQL = this.state.data.map((item, index)=>{
//     console.log(this.state.data);
//     var array = ['Name: ',item.Name,', Breed: ', item.Breed, ' , Gender: ', item.Gender, ', Size: ', item.Size].join(' ');
//     console.log(array)
//     return <p key={index}>{array}</p>;
//   })
//   return (
//    <div className="container">
//    <Zoom>
//      <center style={{margin:'25px'}}>
//         <Flip><h3>MagicHappens ♥♥</h3></Flip>
     
//      <form>

//   <div className="form-group" style={{margin:'15px'}}>
//     <input className="form-control" type="text" id="name" 
//     ref={ inname => this.inputname = inname }
//     placeholder="Input the name here!"/>
//   </div>
//   <div className="form-group" style={{margin:'15px'}}>
//     <input className="form-control" type="text" id="breed" 
//     ref={ inbreed => this.inputbreed = inbreed }
//     placeholder="Input the breed here!"/>
//   </div>
//   <div className="form-group" style={{margin:'15px'}}>
//     <input className="form-control" type="text" id="gender" 
//     ref={ ingender => this.inputgender = ingender }
//     placeholder="Input the gender here!"/>
//   </div>

//   <div className="form-group" style={{margin:'15px'}}>
//     <input className="form-control" type="text" id="size" 
//     ref={ insize => this.inputsize = insize}
//     placeholder="Input size here!"/>
//   </div>
  
//   <button className="btn btn-primary" style={{width:'100px'}}
//   onClick={this.ClickPost.bind(this)}>POST</button>
  
//   <button className="btn btn-success" style={{margin:'15px',width:'100px'}}
//   onClick={this.ClickGet.bind(this)}>GET</button>



// </form>

//      <div>
//        { dataMySQL }
//      </div>
//      </center>
//      </Zoom>
//    </div>
  // );


  }
 }
 
export default App;