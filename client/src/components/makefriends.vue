<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Users Relations</h1>
        <hr><br><br>
        <button
          type="button"
          class="btn btn-success btn-sm"
          @click="toggleAddUserModal">
          Add User
        </button>
        <br><br>
        <button
          type="button"
          class="btn btn-success btn-sm"
          @click="toggleUpdateUserModal">
          Update User
        </button>
        <br><br>
        <p>
        Current user ID: {{currentUserId}}
        </p>
        <br><br>
        <button
          type="button"
          class="btn btn-success btn-sm"
          @click="deleteUser">
          Delete User
        </button>
        <br><br>
        <button
          type="button"
          class="btn btn-success btn-sm"
          @click="toggleShowUserFriendsModal">
          Display Friends
        </button>
        <br><br>
        <button
          type="button"
          class="btn btn-success btn-sm"
          @click="toggleFindFriendsModal">
          Find Friends
        </button>
      </div>
    </div>
    
    <!-- add new user modal -->
<div
  ref="addUserModal"
  class="modal fade"
  :class="{ show: activeAddUserModal, 'd-block': activeAddUserModal }"
  tabindex="-1"
  role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Add a new user</h5>
        <button
          type="button"
          class="close"
          data-dismiss="modal"
          aria-label="Close"
          @click="toggleAddUserModal">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <form>
          <div class="mb-3">
            <label for="addUserUsername" class="form-label">Username:</label>
            <input
              type="text"
              class="form-control"
              id="addUserUsername"
              v-model="AddUserFormData.username"
              placeholder="Enter username">
          </div>
          <div class="mb-3">
            <label for="addUserEmail" class="form-label">Email:</label>
            <input
              type="text"
              class="form-control"
              id="addUserEmail"
              v-model="AddUserFormData.email"
              placeholder="Enter email">
          </div>
          <div class="mb-3">
            <label for="addUserPassword" class="form-label">Password:</label>
            <input
              type="text"
              class="form-control"
              id="addUserPassword"
              v-model="AddUserFormData.password"
              placeholder="Enter password">
          </div>
          <div class="mb-3">
            <label for="addUserCountry" class="form-label">Country:</label>
            <input
              type="text"
              class="form-control"
              id="addUserCountry"
              v-model="AddUserFormData.country"
              placeholder="Enter country">
          </div>
          <div class="mb-3">
            <label for="addUserCity" class="form-label">City:</label>
            <input
              type="text"
              class="form-control"
              id="addUserCity"
              v-model="AddUserFormData.city"
              placeholder="Enter city">
          </div>
          <div class="btn-group" role="group">
            <button
              type="button"
              class="btn btn-primary btn-sm"
              @click="handleAddSubmit">
              Submit
            </button>
            <button
              type="button"
              class="btn btn-danger btn-sm"
              @click="handleAddReset">
              Reset
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</div>
<div v-if="activeAddUserModal" class="modal-backdrop fade show"></div>


    <!-- update user modal -->
<div
  ref="updateUserModal"
  class="modal fade"
  :class="{ show: activeUpdateUserModal, 'd-block': activeUpdateUserModal }"
  tabindex="-1"
  role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Update user data</h5>
        <button
          type="button"
          class="close"
          data-dismiss="modal"
          aria-label="Close"
          @click="toggleUpdateUserModal">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <form>
          <div class="mb-3">
            <label for="updateUserUsername" class="form-label">Username:</label>
            <input
              type="text"
              class="form-control"
              id="updateUserUsername"
              v-model="UpdateUserFormData.username"
              :placeholder="[[ UserData.username ]]">
          </div>
          <div class="mb-3">
            <label for="updateUserEmail" class="form-label">Email:</label>
            <input
              type="text"
              class="form-control"
              id="updateUserEmail"
              v-model="UpdateUserFormData.email"
              :placeholder="[[ UserData.email ]]">
          </div>
          <div class="mb-3">
            <label for="updateUserPassword" class="form-label">Password:</label>
            <input
              type="text"
              class="form-control"
              id="updateUserPassword"
              v-model="UpdateUserFormData.password"
              :placeholder="[[ UserData.password ]]">
          </div>
          <div class="mb-3">
            <label for="updateUserCountry" class="form-label">Country:</label>
            <input
              type="text"
              class="form-control"
              id="updateUserCountry"
              v-model="UpdateUserFormData.country"
              :placeholder="[[ UserData.country ]]">
          </div>
          <div class="mb-3">
            <label for="updateUserCity" class="form-label">City:</label>
            <input
              type="text"
              class="form-control"
              id="updateUserCity"
              v-model="UpdateUserFormData.city"
              :placeholder="[[ UserData.city ]]">
          </div>
          <div class="btn-group" role="group">
            <button
              type="button"
              class="btn btn-primary btn-sm"
              @click="handleUpdateSubmit">
              Submit
            </button>
            <button
              type="button"
              class="btn btn-danger btn-sm"
              @click="handleUpdateReset">
              Reset
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</div>
<div v-if="activeUpdateUserModal" class="modal-backdrop fade show"></div>



    <!-- show user friends modal -->
<div
  ref="ShowUserFriendsModal"
  class="modal fade"
  :class="{ show: activeShowUserFriendsModal, 'd-block': activeShowUserFriendsModal }"
  tabindex="-1"
  role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Friends</h5>
        <button
          type="button"
          class="close"
          data-dismiss="modal"
          aria-label="Close"
          @click="toggleShowUserFriendsModal">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <form>
          
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Email</th>
              <th scope="col">Country</th>
              <th scope="col">City</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(friend, index) in friends" :key="index">
              <td>{{ friend.username }}</td>
              <td>{{ friend.email }}</td>
              <td>{{ friend.country }}</td>
              <td>{{ friend.city }}</td>
            </tr>
          </tbody>
        </table>
        
        </form>
      </div>
    </div>
  </div>
</div>
<div v-if="activeShowUserFriendsModal" class="modal-backdrop fade show"></div>



    <!-- find friends by interests and make friendship modal -->
<div
  ref="FindFriendsModal"
  class="modal fade"
  :class="{ show: activeFindFriendsModal, 'd-block': activeFindFriendsModal }"
  tabindex="-1"
  role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Find your friends!</h5>
        <button
          type="button"
          class="close"
          data-dismiss="modal"
          aria-label="Close"
          @click="toggleFindFriendsModal">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <form>
          <div class="mb-3">
            <label for="potentialFriendsCountry" class="form-label">Country:</label>
            <input
              type="text"
              class="form-control"
              id="potentialFriendsCountry"
              v-model="FindingFriendsCriterias.country"
              placeholder="Enter country">
            <label for="potentialFriendsInterests" class="form-label">Interests:</label>
            <input
              type="text"
              class="form-control"
              id="potentialFriendsInterests"
              v-model="FindingFriendsCriterias.interests"
              placeholder="Enter interests separated by comma">
            <br><br>
           <button
              type="button"
              class="btn btn-success btn-sm"
              @click="getPotentialFriends">
              Find!
           </button>
          <br>
          </div>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Interests</th>
              <th scope="col">City</th>
              <th scope="col">Become friends</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(potential_friend, index) in potential_friends" :key="index">
              <td>{{ potential_friend.username }}</td>
              <td>{{ potential_friend.interests }}</td>
              <td>{{ potential_friend.city }}</td>
              <td><button
          	type="button"
          	class="btn btn-success btn-sm"
          	@click="potential_friend.makeFriendship.call(potential_friend)">
          	Become friends
              </button></td>
            </tr>
          </tbody>
        </table>
        
        </form>
      </div>
    </div>
  </div>
</div>
<div v-if="activeFindFriendsModal" class="modal-backdrop fade show"></div>


  </div>
</template>
  
  
<script>
import axios from 'axios';

class PotentialFriend{
 
  constructor(user_id, username, interests, city, initiatorUserId, conn_addr_string) {
    this.conn_addr_string = conn_addr_string,
    this.user_id = user_id;
    this.username = username;
    this.interests = interests;
    this.city = city;
    this.initiatorUserId = initiatorUserId;
  }
  
  makeFriendship(){
    console.log(this.initiatorUserId, ' -> ',this.user_id);
    
    if(isNaN(parseInt(this.initiatorUserId)) == false)
    {
	const path = this.conn_addr_string + '/friendships';
        
        const payload = { user_id: parseInt(this.initiatorUserId), friend_id: this.user_id };
	axios.post(path, payload)
          .then((res) => {
            alert(res.data['message']);
          })
          .catch((error) => {
            console.log(error);
          });
    }
  }
}


export default {
  name: 'makefriends',
  data() {
    return {
      conn_addr_string : import.meta.env.VITE_SERVER_CONNECT_STRING,
      
      currentUserId: 'Not registered',
      activeAddUserModal: false,
      activeUpdateUserModal: false,
      activeShowUserFriendsModal: false,
      activeFindFriendsModal: false,
      
      UserData: {
        username: '',
        email: '',
        password: '',
        country: '',
        city: '',
      },
      
      AddUserFormData: {
        username: '',
        email: '',
        password: '',
        country: '',
        city: '',
      },
      
      UpdateUserFormData: {
        username: '',
        email: '',
        password: '',
        country: '',
        city: '',
      },
      
      friends: [],
      potential_friends: [],
      
      FindingFriendsCriterias: {
        country: '',
        interests: '',
      },
      
    };
  },
  methods: {
    // add user
    addUser(payload) {
      const path = this.conn_addr_string + '/users';
      
      this.UserData.username = this.AddUserFormData.username;
      this.UserData.email = this.AddUserFormData.email;
      this.UserData.password = this.AddUserFormData.password;
      this.UserData.country = this.AddUserFormData.country;
      this.UserData.city = this.AddUserFormData.city;
      
      axios.post(path, payload)
        .then((res) => {
          console.log(res);
          this.currentUserId = res.data['user_id'];
          alert(res.data['message']);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    handleAddReset() {
      this.initAddUserForm();
    },
    handleAddSubmit() {
      this.toggleAddUserModal();
      
      const payload = {
        username:  this.AddUserFormData.username,
        email: this.AddUserFormData.email,
        password: this.AddUserFormData.password,
        country: this.AddUserFormData.country,
        city: this.AddUserFormData.city,
      };
      
      this.addUser(payload);
      this.initAddUserForm();
      
      console.log(this.UserData);
    },
    initAddUserForm() {
      this.AddUserFormData.username = '';
      this.AddUserFormData.email = '';
      this.AddUserFormData.password = '';
      this.AddUserFormData.country = '';
      this.AddUserFormData.city = '';
    },
    toggleAddUserModal() {
      console.log(this.conn_addr_string);
    
      const body = document.querySelector('body');
      this.activeAddUserModal = !this.activeAddUserModal;
      if (this.activeAddUserModal) {
        body.classList.add('modal-open');
      } else {
        body.classList.remove('modal-open');
      }
    },
    
    // update user
    updateUser(payload) {
    
    if(isNaN(parseInt(this.currentUserId)) == false)
    {
        const path = this.conn_addr_string + `/users/${parseInt(this.currentUserId)}`;
        
        if (this.UpdateUserFormData.username != '') {
        	this.UserData.username  = this.UpdateUserFormData.username;
      	}
      	if (this.UpdateUserFormData.email != '') {
        	this.UserData.email = this.UpdateUserFormData.email;
      	}
      	if (this.UpdateUserFormData.password != '') {
        	this.UserData.password = this.UpdateUserFormData.password;
      	}
      	if (this.UpdateUserFormData.country != '') {
		this.UserData.country = this.UpdateUserFormData.country;
      	}
      	if (this.UpdateUserFormData.city != '') {
        	this.UserData.city = this.UpdateUserFormData.city;
      	}
                
      	axios.patch(path, payload)
        	.then((res) => {
        	alert(res.data['message']);
        	})
        	.catch((error) => {
          	console.log(error);
        	});
    }
    },
    handleUpdateReset() {
      this.initUpdateUserForm();
    },
    handleUpdateSubmit() {
      this.toggleUpdateUserModal();
      const payload = Object.create(null);
      
      if (this.UpdateUserFormData.username != '') {
        payload['username'] = this.UpdateUserFormData.username;
      }
      if (this.UpdateUserFormData.email != '') {
        payload['email'] = this.UpdateUserFormData.email;
      }
      if (this.UpdateUserFormData.password != '') {
        payload['password'] = this.UpdateUserFormData.password;
      }
      if (this.UpdateUserFormData.country != '') {
        payload['country'] = this.UpdateUserFormData.country;
      }
      if (this.UpdateUserFormData.city != '') {
        payload['city'] = this.UpdateUserFormData.city;
      }
      
      this.updateUser(payload);
      this.initUpdateUserForm();
    },
    
    initUpdateUserForm() {
      this.UpdateUserFormData.username = '';
      this.UpdateUserFormData.email = '';
      this.UpdateUserFormData.password = '';
      this.UpdateUserFormData.country = '';
      this.UpdateUserFormData.city = '';
    },
    
    toggleUpdateUserModal() {
      const body = document.querySelector('body');
      this.activeUpdateUserModal = !this.activeUpdateUserModal;
      if (this.activeUpdateUserModal) {
        body.classList.add('modal-open');
      } else {
        body.classList.remove('modal-open');
      }
    },
    
    // show user friends
    getListOfUserFriends() {
    if(isNaN(parseInt(this.currentUserId)) == false)
      {
        const path = this.conn_addr_string + `/friends/${parseInt(this.currentUserId)}`;
        axios.get(path, { params: { limit: 20, offset: 0 } })
          .then((res) => {
            console.log(res);
            this.friends = res.data['data'];
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
    
    toggleShowUserFriendsModal() {
      const body = document.querySelector('body');
      this.activeShowUserFriendsModal = !this.activeShowUserFriendsModal;
      if (this.activeShowUserFriendsModal) {
      	this.getListOfUserFriends();
        body.classList.add('modal-open');
      } else {
        body.classList.remove('modal-open');
      }
    },
    
    // find friends
    getPotentialFriends() {
        const path = this.conn_addr_string + '/friends/search';
        axios.get(path, { params: { country: this.FindingFriendsCriterias.country, interests: this.FindingFriendsCriterias.interests } })
          .then((res) => {
            console.log(res);
            //console.log(res.data['data']);
            //console.log(res.data['data'].length);
            var length = res.data['data'].length;
    	    var element = null;
    
	    this.potential_friends = [];
    
            for (var i = 0; i < length; i++) {
  		element = res.data['data'][i];
  		console.log(element);
  		this.potential_friends.push(new PotentialFriend(element['id'], element['username'], element['interests'], element['city'], this.currentUserId, this.conn_addr_string));
	    }
	    console.log(this.potential_friends);
          })
          .catch((error) => {
            console.log(error);
          });
    },
    
    toggleFindFriendsModal() {
      const body = document.querySelector('body');
      this.activeFindFriendsModal = !this.activeFindFriendsModal;
      if (this.activeFindFriendsModal) {
        body.classList.add('modal-open');
      } else {
        body.classList.remove('modal-open');
      }
    },
    
    //delete user
    deleteUser() {
      if(isNaN(parseInt(this.currentUserId)) == false)
      {
        const path = this.conn_addr_string + `/users/${parseInt(this.currentUserId)}`;
        axios.delete(path)
          .then((res) => {
            this.currentUserId = 'Not registered';
            this.UserData.username = '';
            this.UserData.email = '';
            this.UserData.password = '';
            this.UserData.country = '';
            this.UserData.city = '';
            
            alert(res.data['message']);
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  },
};
</script>


