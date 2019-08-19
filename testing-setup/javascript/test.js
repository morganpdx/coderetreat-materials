const assert = require('assert')

const hello = require('./hello.js')

it('should return true', () => {
  assert.equal(true, false)
})

it('returns Hello World', () => {
    assert.equal(hello(), 'Hello World')
  })