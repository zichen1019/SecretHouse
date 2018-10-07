import request from '@/utils/request'

//更新属性
export function updateAttribute(data) {
  return request({
    url: '/api/attr/updateAttribute',
    method: 'post',
    data: data
  })
}

// 获取属性
export function getAttribute(query) {
  return request({
    url: '/api/attr/getAttribute',
    method: 'get',
    params: query
  })
}

// 获取某人属性
export function getAttributeList(query) {
  return request({
    url: '/api/getUserAttrList',
    method: 'get',
    params: query
  })
}