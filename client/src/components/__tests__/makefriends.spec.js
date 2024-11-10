import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import makefriends from '../makefriends.vue'


import { setupServer } from 'msw/node'
import { HttpResponse, http  } from 'msw'

import { test, expect, beforeAll, afterEach, afterAll } from "vitest";



describe('makefriends', () => {
  it('renders properly', () => {
    const wrapper = mount(makefriends)
    expect(wrapper.text()).toContain('Add User')
    expect(wrapper.text()).toContain('Update User')
    expect(wrapper.text()).toContain('Delete User')
    expect(wrapper.text()).toContain('Display Friends')
    expect(wrapper.text()).toContain('Find Friends')
  })
})


export const restHandlers = [
http.get('http://127.0.0.1:5015/friends/search', () => {

  return new HttpResponse(JSON.stringify([
      {
        user_id: 23,
        username: 'k5n6jk',
        email: '2nk3njk2',
        country: 'g5kgn4k5',
        city: 'k4nk3nkjk4',
      },
      {
        user_id: 17,
        username: 'n45n4o6',
        email: 'm,mevrever',
        country: 'btbtkb',
        city: 'btkk5k',
      },
      {
        user_id: 9,
        username: 'ekrm',
        email: 'tbtb',
        country: 'l6o5m6',
        city: '96b6jbje',
      },
      {
        user_id: 78,
        username: 'mob',
        email: 'm 5k64',
        country: 'ewc',
        city: '5k4jnjk64',
      },
      ]))
})
]
const server = setupServer(...restHandlers)
// Start server before all tests
beforeAll(() => server.listen({ onUnhandledRequest: 'error' }))

//  Close server after all tests
afterAll(() => server.close())

// Reset handlers after each test `important for test isolation`
afterEach(() => server.resetHandlers())


test("Emptiness of lists of friends and potential friends after initialisation", () => {
  expect(makefriends).toBeTruthy();
    
  const wrapper = mount(makefriends);
  
  expect(wrapper.vm.friends).toEqual([]);
  expect(wrapper.vm.potential_friends).toEqual([]);
});

test("User is not registered after initialisation", () => {
  expect(makefriends).toBeTruthy();
    
  const wrapper = mount(makefriends);
  
  //console.log(wrapper.vm);
  expect(wrapper.vm.currentUserId).toEqual("Not registered");
});


function sleep(milliseconds) {
  const date = Date.now();
  let currentDate = null;
  do {
    currentDate = Date.now();
  } while (currentDate - date < milliseconds);
}
 
test("Get potential friends", async () => {
  expect(makefriends).toBeTruthy();
    
  const wrapper = mount(makefriends);
  wrapper.vm.FindingFriendsCriterias = { country: '34r5', interests: 'ervrevrv' }
  
  console.log(wrapper.vm.FindingFriendsCriterias);
  console.log('I GOT <<', wrapper.vm.getPotentialFriends.call());
  console.log(wrapper.vm.potential_friends);
});
