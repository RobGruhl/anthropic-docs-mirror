## Delete

**delete** `/v1/organizations/users/{user_id}`

Remove User

### Path Parameters

- `user_id: string`

  ID of the User.

### Returns

- `id: string`

  ID of the User.

- `type: "user_deleted"`

  Deleted object type.

  For Users, this is always `"user_deleted"`.

  - `"user_deleted"`


---
📖 **Source:** https://platform.claude.com/docs/en/api/admin/users/delete
*Mirrored from platform.claude.com for local access.*
