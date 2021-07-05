import React from 'react'
import axios from 'axios'
import { Switch, message } from 'antd'
import TableWithModal from '../components/TableWithModal'
import Wrapper from '../components/Wrapper'
const lightStateDisplay = (light_state, record) => (
  <Switch
    key={light_state}
    defaultChecked={light_state}
    checkedChildren='on'
    unCheckedChildren='off'
    onChange={(_light_state) =>
      axios
        .post(`http://${process.env.NEXT_PUBLIC_API_URL}:8000/update_light`, {
          light_state: _light_state,
          id: record.id,
        })
        .then(async (response) => {
          message.success(response.data.message)
          return response
        })
        .catch((error) => error)
    }
  />
)
const columns = [
  {
    title: 'Light Name',
    dataIndex: 'light_name',
    key: 'light_name',
  },
  {
    title: 'Light Status',
    dataIndex: 'light_state',
    key: 'light_state',
    render: lightStateDisplay,
  },
  {
    title: 'Light Color',
    dataIndex: 'light_color',
    key: 'light_color',
  },
]
const Lights = () => (
  <Wrapper title={'Lights'}>
    <TableWithModal
      columns={columns}
      eventKey={'light'}
      getKey={'lights'}
      key={'light'}
    />
  </Wrapper>
)
export default Lights
