import React, { useState, useEffect } from 'react'
import axios from 'axios'
import { Table } from 'antd'
import styles from '../styles/Home.module.css'
import Wrapper from '../components/Wrapper'
const columns = [
  {
    title: 'Appliance Name',
    dataIndex: 'applianceName',
    key: 'applianceName',
  },
  {
    title: 'Appliance Type',
    dataIndex: 'applianceType',
    key: 'applianceType',
  },
  {
    title: 'Event Type',
    dataIndex: 'eventType',
    key: 'eventType',
  },
  {
    title: 'Event Description',
    dataIndex: 'description',
    key: 'description',
  },
  {
    title: 'Time Stamp',
    dataIndex: 'createdOn',
    key: 'createdOn',
  },
]
const LogHistory = () => {
  const [dataSource, setDataSource] = useState()
  const getData = async () =>
    await axios
      .get(`http://${process.env.NEXT_PUBLIC_API_URL}:8000/logs`)
      .then((response) => {
        setDataSource(response.data)
        return response
      })
      .catch((error) => error)
  useEffect(() => getData(), [])
  return (
    <Wrapper title={'Log History'}>
      <main className={styles.main}>
        <Table
          rowKey='id'
          className='no-border-last'
          pagination={{
            defaultPageSize: 20,
            showSizeChanger: true,
            responsive: true,
            pageSizeOptions: [20, 50, 100, 200, 400],
          }}
          scroll={{
            x: 500,
            y: 'calc(100vh - 370px)',
            scrollToFirstRowOnChange: false,
          }}
          columns={columns}
          dataSource={dataSource}
        />
      </main>
    </Wrapper>
  )
}
export default LogHistory
