import React, { useEffect, useCallback } from 'react'
import { Modal, Form, Input, Switch, Radio } from 'antd'
const CreateForm = ({
  eventKey,
  visible,
  onCreate,
  onCancel,
  defaultFormValues,
  isEditForm,
  form,
}) => {
  const formProps = {
    thermostat: [
      {
        name: 'thermostat_name',
        label: 'Thermostat name',
        rules: [
          {
            required: true,
            message: 'Please input the name of thermostat!',
          },
        ],
        renderComponent: (
          <Input disabled={isEditForm} placeholder={'ex. Kitchen'} />
        ),
      },
      {
        name: 'temperature',
        label: 'Temperature',
        rules: [
          {
            required: true,
            message: 'Please input the name of thermostat!',
          },
        ],
        renderComponent: <Input placeholder={'ex. 105'} suffix={'F'} />,
      },
    ],
    light: [
      {
        name: 'light_name',
        label: 'Light name',
        rules: [
          {
            required: true,
            message: 'Please input the name of light!',
          },
        ],
        renderComponent: (
          <Input disabled={isEditForm} placeholder={'ex. Kitchen Light'} />
        ),
      },
      {
        name: 'light_state',
        label: 'Light state',
        rules: [
          {
            required: false,
          },
        ],
        renderComponent: (
          <Switch
            defaultChecked={defaultFormValues?.light_state || false}
            checkedChildren='on'
            unCheckedChildren='off'
            key={Math.random()}
          />
        ),
      },
      {
        name: 'light_color',
        label: 'Light color',
        rules: [
          {
            required: true,
            message: 'Please select the light color!',
          },
        ],
        renderComponent: (
          <Radio.Group disabled={isEditForm}>
            {['red', 'orange', 'yellow', 'green', 'blue'].map((value) => (
              <Radio.Button key={value} value={value}>
                {value.toUpperCase()}
              </Radio.Button>
            ))}
          </Radio.Group>
        ),
      },
    ],
  }
  const resetBusiness = () => {
    form.resetFields()
    if (defaultFormValues) form.setFieldsValue(defaultFormValues)
  }
  useEffect(() => {
    resetBusiness()
  }, [defaultFormValues])
  return (
    <Modal
      visible={visible}
      title={`${
        isEditForm ? `Update ${eventKey}` : `Create a new ${eventKey}`
      } `}
      okText={isEditForm ? 'Update' : 'Create'}
      cancelText='Cancel'
      onCancel={() => {
        form.resetFields()
        onCancel()
      }}
      onOk={() => {
        form
          .validateFields()
          .then((values) => onCreate(values))
          .catch((info) => info)
      }}
    >
      <Form
        initialValues={{
          light_state: false,
        }}
        form={form}
        layout='vertical'
        name='form_in_modal'
      >
        {formProps[eventKey].map(({ label, name, rules, renderComponent }) => (
          <Form.Item key={name} label={label} name={name} rules={rules}>
            {renderComponent}
          </Form.Item>
        ))}
      </Form>
    </Modal>
  )
}
export default CreateForm
