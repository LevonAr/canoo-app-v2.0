import React, { useState, useEffect } from 'react'
import { Menu, Layout } from 'antd'
import Router from 'next/router'
import Image from 'next/image'
import { useRouter } from 'next/router'
import MainHead from './head'
const { Header } = Layout
const HeaderComponent = () => {
  const router = useRouter()
  const [selectedKeys, setSelectedKeys] = useState(['/lights'])
  useEffect(() => setSelectedKeys(router.pathname), [router.pathname])
  return (
    <Header
      style={{
        position: 'fixed',
        zIndex: 1,
        width: '100%',
        background: '#fff',
      }}
    >
      <MainHead title={'Canoo'} />
      <a href='https://www.canoo.com' rel='noreferrer' target='_blank'>
        <Image
          src='/logo/canoo-logo.svg'
          alt='https://www.canoo.com'
          layout='fill'
        />
      </a>
      <Menu
        theme='light'
        mode='horizontal'
        onClick={(e) => {
          setSelectedKeys([e.key])
          Router.push(e.key)
        }}
        selectedKeys={selectedKeys}
        selectable
      >
        <Menu.Item key='/lights'>Lights</Menu.Item>
        <Menu.Item key='/thermostats'>Thermostats</Menu.Item>
        <Menu.Item
          style={{
            marginLeft: 'calc(100vw - 450px)',
          }}
          key='/log-history'
        >
          Logs
        </Menu.Item>
      </Menu>
    </Header>
  )
}
export default HeaderComponent
