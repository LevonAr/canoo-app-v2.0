import React from 'react'
import { Card } from 'antd'
import LayoutComponent from '../components/Layout'
const Wrapper = ({ children, title }) => {
  return (
    <LayoutComponent>
      <Card title={title}>{children}</Card>
    </LayoutComponent>
  )
}
export default Wrapper
