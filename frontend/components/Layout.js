import React from 'react'
import { Layout } from 'antd'
import HeaderComponent from './Header'
const { Content } = Layout
const LayoutComponent = (props) => {
  return (
    <Layout>
      <HeaderComponent />
      <Content
        className='site-layout'
        style={{ padding: '0 50px', marginTop: 64, background: '#fff' }}
      >
        <div
          className='site-layout-background'
          style={{ padding: 24, minHeight: '500px' }}
        >
          {props.children}
        </div>
      </Content>
      <style>
        {`
          .site-layout .site-layout-background {
            background: #fff;
          }
        `}
      </style>
    </Layout>
  )
}
export default LayoutComponent
